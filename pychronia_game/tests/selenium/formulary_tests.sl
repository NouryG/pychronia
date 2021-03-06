<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="http://127.0.0.1:8000/" />
<title>formulary_tests</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">formulary_tests</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>http://127.0.0.1:8000/login/</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_secret_username</td>
	<td>master</td>
</tr>
<tr>
	<td>type</td>
	<td>id_secret_password</td>
	<td>ultimate</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>login</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>//form[@id='change_language_en']/a/img</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>http://127.0.0.1:8000/DATABASE_OPERATIONS/?reset_game_data=1</td>
	<td></td>
</tr>
<tr>
	<td>open</td>
	<td>http://127.0.0.1:8000/</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Databases</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>switch_game_state</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Auction</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>buy</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>unbuy</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>buy</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>buy</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>buy</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Characters</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_amount</td>
	<td>600</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>money_transfer</td>
	<td></td>
</tr>
<tr>
	<td>addSelection</td>
	<td>id_gems_choices</td>
	<td>value=134</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>gems_transfer</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>134</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Wiretaps</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_target_0</td>
	<td>label=Emilos Farthstariygta</td>
</tr>
<tr>
	<td>select</td>
	<td>id_target_1</td>
	<td>label=Simon Bladstaffulovza</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>wiretap</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Agents Hiring</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>hire_agents</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_location</td>
	<td>label=Alifir</td>
</tr>
<tr>
	<td>select</td>
	<td>id_type</td>
	<td>label=Mercenaries</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>hire_agents</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>assertElementPresent</td>
	<td>//div[@id='primaryContent']/p[2]</td>
	<td></td>
</tr>
<tr>
	<td>assertText</td>
	<td>//div[@id='primaryContent']/p[3]</td>
	<td>Alifir</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Mercenary Commandos</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_message</td>
	<td>AAAAAAAA</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>intervention</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Teleportations</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_message</td>
	<td>bbbbbbbbbb</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>intervention</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Zealot Attacks</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_message</td>
	<td>ccccccccccc</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>intervention</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Telecom Investigations</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>investigation</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>1</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Translations</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_transcription</td>
	<td>sd sd sd sd</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>Translate</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=World Scans</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_item_name</td>
	<td>label=Two Awesome Diamonds</td>
</tr>
<tr>
	<td>type</td>
	<td>id_description</td>
	<td>ggggg</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>scan</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Manage Webradio</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>turn_radio_on</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>turn_radio_off</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>refresh</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>currently OFF</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>add_audio_message</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>//div[@id='primaryContent']/div[6]/table/tbody/tr[8]/td[2]/a[1]/form/input[2]</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>reset_playlist</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>currently empty</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Messages (4)</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Templates</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Use Template</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>send_message</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Templates</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>already done</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Inbox</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Reply to message</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>arrowSelectBox0</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_body</td>
	<td>ssss</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>send_message</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Inbox</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>already done</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Compose</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>//div[@id='selectBoxOptions0']/div[1]</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>arrowSelectBox1</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>//div[@id='selectBoxOptions1']/div[2]</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_delay_mn</td>
	<td>label=2 minutes</td>
</tr>
<tr>
	<td>type</td>
	<td>id_subject</td>
	<td>kkk</td>
</tr>
<tr>
	<td>type</td>
	<td>id_body</td>
	<td>llll</td>
</tr>
<tr>
	<td>type</td>
	<td>id_attachment</td>
	<td>aaaa</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>send_message</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=All Transferred</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>ggggg</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>sd sd sd</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Investigation Request</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>cccccccccc</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Akarith Attack on Aklarvik</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>bbbbbbbbbb</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Teldorian Teleportation on unscanned location Aklarvi</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>AAAAAAAA</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Mercenary Intervention on Alifir</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Templates</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Use Template</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>send_message</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Oracles</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_djinn</td>
	<td>label=Phayl Blogg</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>contact_djinn</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Phayl Blogg</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>msgbox</td>
	<td>where is cynthia ?</td>
</tr>
<tr>
	<td>keyPress</td>
	<td>msgbox</td>
	<td>\13</td>
</tr>
<tr>
	<td>waitForTextPresent</td>
	<td>struggle for power</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Radio Applet</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_frequency</td>
	<td>100.0</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>listen_radio</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>assertElementPresent</td>
	<td>id=niftyPlayer1</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Logout</td>
	<td></td>
</tr>
<tr>
	<td>type</td>
	<td>id_secret_username</td>
	<td>listener</td>
</tr>
<tr>
	<td>type</td>
	<td>id_secret_password</td>
	<td>aware</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>login</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>//form[@id='change_language_en']/a/img</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Characters</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>id_recipient_name</td>
	<td>label=Docteur Nioutohnkievthijk</td>
</tr>
<tr>
	<td>type</td>
	<td>id_amount</td>
	<td>50</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>money_transfer</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Characters</td>
	<td></td>
</tr>
<tr>
	<td>select</td>
	<td>//div[@id='primaryContent']/div[2]/form/table/tbody/tr[2]/td/select</td>
	<td>label=Docteur Nioutohnkievthijk</td>
</tr>
<tr>
	<td>addSelection</td>
	<td>id_gems_choices</td>
	<td>label=Gem of 129 Kashes</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>gems_transfer</td>
	<td></td>
</tr>
<tr>
	<td>assertTextPresent</td>
	<td>Messages</td>
	<td></td>
</tr>
<tr>
	<td>assertTable</td>
	<td>//div[@id='primaryContent']/table.3.1</td>
	<td>50</td>
</tr>
<tr>
	<td>assertTable</td>
	<td>//div[@id='primaryContent']/table.3.3</td>
	<td>129</td>
</tr>
<tr>
	<td>clickAndWait</td>
	<td>link=Logout</td>
	<td></td>
</tr>

</tbody></table>
</body>
</html>
