# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from pychronia_game.common import *
from pychronia_game.datamanager.abstract_ability import AbstractAbility
from pychronia_game.datamanager.abstract_game_view import register_view
from pychronia_game.datamanager.datamanager_tools import readonly_method, \
    transaction_watcher
from pychronia_game.forms import OtherCharactersForm


BROKEN ATM 


# TODO - make randomness constant between retries, thanks to game_random_seed parameter #

@register_view
class TelecomInvestigationAbility(AbstractAbility):

    TITLE = ugettext_lazy("Telecom Investigation")
    NAME = "telecom_investigation"

    GAME_ACTIONS = dict(investigation_form=dict(title=ugettext_lazy("Process telecom investigation"),
                                              form_class=OtherCharactersForm,
                                              callback="process_telecom_investigation"))

    TEMPLATE = "abilities/telecom_investigation.html"

    ACCESS = UserAccess.character
    REQUIRES_CHARACTER_PERMISSION = True
    REQUIRES_GLOBAL_PERMISSION = True


    @classmethod
    def _setup_ability_settings(cls, settings):
        pass # nothing to do

    def _setup_private_ability_data(self, private_data):
        pass # nothing to do

    def _check_data_sanity(self, strict=False):
        pass # nothing to do



    def get_template_vars(self, previous_form_data=None):

        translation_form = self._instantiate_game_form(new_action_name="investigation_form",
                                                  hide_on_success=False,
                                                  previous_form_data=previous_form_data)

        translation_delay = (2, 3) # FIXME TODO self.get_ability_parameter("result_delay")  # TODO - translate this

        return {
                 'page_title': _("Telecom Investigation"),
                 "investigation_form": translation_form,
                 'min_delay_mn': translation_delay[0],
                 'max_delay_mn': translation_delay[1],
               }



    @staticmethod
    def _corrupt_text_parts(text, corrupted_chunks_lengths, key_phrase=""):
        # Words of "key_phrase" will NECESSARILY be found in final corrupted message, if they exist in original message

        keywords = key_phrase.lower().split()
        words = text.split()

        result = []
        must_add = True

        while words:
            length = random.randint(corrupted_chunks_lengths[0], corrupted_chunks_lengths[1])
            selected_words = words[0:length]
            selected_words_lower = " ".join(selected_words).lower()  # string, to avoid problems with punctuation marks
            words = words[length:]

            for key in keywords:
                if key in selected_words_lower:
                    must_add = True
                    break

            if must_add:
                result += selected_words
            else:
                result += ["..."]
            must_add = not must_add

        return " ".join(result)


    @readonly_method
    def _get_corrupted_introduction(self, target_username, key_phrase):
        # Words of "key_phrase" will NECESSARILY be found in final corrupted message, if they exist in original message

        from django.utils.html import strip_tags

        chunk_lengths = self.get_global_parameter("corrupted_chunks_lengths")
        result = "\n"

        raw_team_intro = self.get_game_instructions(target_username)["team_introduction"]
        if raw_team_intro:
            team_introductions = raw_team_intro.split(
                "<hr/>")  # some teams like akariths have several parts in their intro
            intro_chunks = [self._corrupt_text_parts(strip_tags(intro), chunk_lengths, key_phrase) for intro in
                            team_introductions]
            result += "\n\n------------\n\n".join(intro_chunks)

        instructions = [msg for msg in self.get_all_dispatched_messages() if msg["id"] == "instructions_" + target_username]
        if instructions:
            if raw_team_intro:
                result += "\n\n------------\n\n"
            instruction = instructions[0]
            result += "**" + _("Message") + "**" + "\n\n" + _("From: ") + instruction["sender_email"] + "\n\n" + _(
                "To: ") + str(instruction["recipient_emails"]) + \
                      "\n\n" + _("Subject: ") + instruction["subject"] + "\n\n"
            result += "\n" + self._corrupt_text_parts(instruction["body"], chunk_lengths, key_phrase)
        else:
            self.logger.error("Player instructions message for %s not found !" % target_username, exc_info=True)

        return result


    @transaction_watcher
    def process_telecom_investigation(self, target_username, use_gems=()):

        username = self.datamanager.user.username
        target_official_name = self.get_official_name(target_username)

        if target_username == username:
            raise UsageError(_("Opening an inquiry into yourself doesn't make much sense."))

        remote_email = "investigator@special.com"  # dummy domain too
        local_email = self.get_character_email()


        # request email to allow interception

        subject = _("Investigation Request for character %(target_official_name)s") % \
                  SDICT(target_official_name=target_official_name)
        body = _("Please let me know anything you may discover about this individual.")
        self.post_message(local_email, remote_email, subject, body, date_or_delay_mn=0)


        # answer email

        subject = _('<Inquiry Results for %(target_official_name)s>') % \
                  SDICT(target_official_name=target_official_name)

        body = self._get_corrupted_introduction(target_username, target_official_name)

        attachment = None

        msg_id = self.post_message(remote_email, local_email, subject, body, attachment,
                                   date_or_delay_mn=self.get_global_parameter("telecom_investigation_delays"))

        self.log_game_event(ugettext_noop('Character inquiry opened into %(target_official_name)s'),
                             PersistentMapping(target_official_name=target_official_name),
                             url=self.get_message_viewer_url_or_none(msg_id),
                             visible_by=None)

        return _("Telecom investigation is in process, you'll receive the result by email.")


'''
            elif name == "corrupted_chunks_lengths":
                assert len(value) == 2 and (value[0] <= value[1])
                assert isinstance(value[0], (int, long))
                assert isinstance(value[1], (int, long))



###corrupted_chunks_lengths
'''
