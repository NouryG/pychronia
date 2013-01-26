# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from rpgweb.common import *
from rpgweb.datamanager import AbstractGameView, register_view, AbstractGameForm
from rpgweb.authentication import authenticate_with_credentials, logout_session
from django.http import HttpResponseRedirect
from rpgweb import forms


@register_view(access=UserAccess.anonymous, always_available=True)
def login(request, template_name='registration/login.html'):

    form = None
    user = request.datamanager.user

    if request.method == "POST":
        if not request.session.test_cookie_worked():
            user.add_error(_("Your Web browser might have cookies disabled. Cookies are required to properly log in."))

        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["secret_username"].strip()
            password = form.cleaned_data["secret_password"].strip()

            if request.POST.get("password_forgotten", None): # password recovery system
                with action_failure_handler(request, success_message=None):
                    request.datamanager.get_secret_question(username)  # check that it's OK
                    return HttpResponseRedirect(reverse(secret_question, kwargs=dict(game_instance_id=request.datamanager.game_instance_id, concerned_username=username)))

            else:  # normal authentication
                with action_failure_handler(request, _("You've been successfully logged in.")):  # message won't be seen because of redirect...
                    authenticate_with_credentials(request, username, password)
                    return HttpResponseRedirect(reverse("rpgweb-homepage", kwargs=dict(game_instance_id=request.datamanager.game_instance_id)))

    else:
        request.session.set_test_cookie()
        form = forms.AuthenticationForm()

    return render(request,
                  template_name,
                    {
                     'page_title': _("User Authentication"),
                     'login_form': form
                    })


@register_view(access=UserAccess.authenticated, always_available=True)
def logout(request, template_name='registration/logout.html'):

    logout_session(request)

    user = request.datamanager.user  # take user only NOW, after logout
    user.add_message(_("You've been successfully logged out."))  # will not be seen with redirection
    return HttpResponseRedirect(reverse(login, kwargs=dict(game_instance_id=request.datamanager.game_instance_id)))




@register_view(access=UserAccess.anonymous)
def secret_question(request, concerned_username, template_name='registration/secret_question.html'):

    secret_question = None
    form = None

    try:
        secret_question = request.datamanager.get_secret_question(concerned_username)
    except UsageError:
        request.datamanager.user.add_error(_("You must provide a valid username to recover your password"))
        return HttpResponseRedirect(reverse("rpgweb-homepage", kwargs=dict(game_instance_id=request.datamanager.game_instance_id)))


    if request.method == "POST" and request.POST.get("recover", None):

        # WARNING - manual validation, so that secret answer is checked BEFORE email address
        secret_answer_attempt = request.POST.get("secret_answer", None)
        if secret_answer_attempt:
            secret_answer_attempt = secret_answer_attempt.strip()
        target_email = request.POST.get("target_email", None)
        if target_email:
            target_email = target_email.strip()

        with action_failure_handler(request, _("Your password has been successfully emailed to your backup address.")):
            try:
                request.datamanager.process_secret_answer_attempt(concerned_username, secret_answer_attempt, target_email)  # raises error on bad answer/email
                # success
                secret_question = None
                form = None

            except:
                form = forms.SecretQuestionForm(concerned_username, data=request.POST)
                form.full_clean()
                raise

    else:
        form = forms.SecretQuestionForm(concerned_username)

    assert (not form and not secret_question) or (form and secret_question)

    return render(request,
                  template_name,
                    {
                     'page_title': _("Password Recovery"),
                     'concerned_username': concerned_username,
                     'secret_question': secret_question,
                     'secret_question_form': form,
                    })









@register_view
class CharacterProfile(AbstractGameView):

    NAME = "character_profile"
    TEMPLATE = "registration/character_profile.html"
    ACCESS = UserAccess.character
    ALWAYS_AVAILABLE = True

    GAME_FORMS = {"password_change_form": (forms.PasswordChangeForm, "process_password_change_form")}


    def get_template_vars(self, previous_form_data=None):

        character_properties = self.datamanager.get_character_properties(self.datamanager.user.username)

        password_change_form = self._instantiate_form(new_form_name="password_change_form",
                                                      hide_on_success=False,
                                                      previous_form_data=previous_form_data)

        return {
                 'page_title': _("User Profile"),
                 "character_properties": character_properties,
                 'password_change_form': password_change_form,
               }


    def process_password_change_form(self, old_password, new_password1, new_password2):
        assert old_password and new_password1 and new_password2
        assert self.datamanager.user.is_character

        if new_password1 != new_password2:
            raise AbnormalUsageError(_("New passwords not matching")) # will be logged as critical - shouldn't happen due to form checks

        self.datamanager.process_password_change_attempt(self.datamanager.user.username, old_password, new_password1)

        return _("Password change successfully performed.")

character_profile = CharacterProfile.as_view






@register_view
class FriendshipManagementAbility(AbstractGameView):


    NAME = "friendship_management"

    GAME_FORMS = {}
    ACTIONS = {"do_propose_friendship": "do_propose_friendship",
               "do_accept_friendship": "do_accept_friendship",
               "do_cancel_proposal" : "do_cancel_proposal",
               "do_cancel_friendship": "do_cancel_friendship"}

    ADMIN_FORMS = {}

    TEMPLATE = "generic_operations/friendship_management.html"

    ACCESS = UserAccess.character
    PERMISSIONS = []
    ALWAYS_AVAILABLE = True


    def _relation_type_to_action(self, relation_type):
        if relation_type == "proposed_to":
            return ("do_cancel_proposal", _("Cancel proposal"))
        elif relation_type == "requested_by":
            return ("do_accept_friendship", _("Accept friendship"))
        elif relation_type == "recent_friend":
            return None
        elif relation_type == "old_friend":
            return ("do_cancel_friendship", _("Abort friendship"))
        else:
            assert relation_type is None, repr(relation_type)
            return ("do_propose_friendship", _("Propose friendship"))


    def get_template_vars(self, previous_form_data=None):

        username = self.datamanager.user.username
        friendship_statuses = self.datamanager.get_other_characters_friendship_statuses(username)


        friendship_actions = sorted([(other_username, self._relation_type_to_action(relation_type))
                                     for (other_username, relation_type) in friendship_statuses.items()]) # list of pairs (other_username, relation_type)

        return {
                 'page_title': _("Friendship Management"),
                 "friendship_actions": friendship_actions,
               }

    def do_propose_friendship(self, other_username):
        res = self.datamanager.propose_friendship(proposer=self.datamanager.user.username,
                                                  recipient=other_username)
        if res:
            return _("You're now friend with %s, as that user concurrently proposed friendship too.") % other_username # should be fairly rare
        else:
            return _("Your friendship proposal to %s has been recorded.") % other_username


    def do_accept_friendship(self, other_username):
        res = self.datamanager.propose_friendship(proposer=self.datamanager.user.username,
                                                  recipient=other_username)
        if res:
            return _("You're now friend with %s.") % other_username
        else:
            return _("Your friendship proposal to user %s has been recorded, as he has cancelled his own friendship proposal.") % other_username  # should be fairly rare


    def do_cancel_proposal(self, other_username):

        res = self.datamanager.terminate_friendship(username=self.datamanager.user.username, # might raise exception if (rare) concurrent cancelation occurred
                                                    rejected_user=other_username)
        if res:
            return _("Your friendship with %s has been properly canceled, as he had accepted it concurrently.") % other_username
        else:

            return _("Your friendship proposal to user %s has been properly canceled.") % other_username


    def do_cancel_friendship(self, other_username):

        res = self.datamanager.terminate_friendship(username=self.datamanager.user.username, # might raise exception if (rare) concurrent cancelation occurred
                                                    rejected_user=other_username)
        if res:
            return _("Your friendship with %s has been properly canceled.") % other_username
        else:
            return _("Your friendship proposal to user %s has been properly canceled.") % other_username  # weirdest case...


friendship_management = FriendshipManagementAbility.as_view
