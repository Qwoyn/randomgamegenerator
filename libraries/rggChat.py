'''
rggChat - for the Random Game Generator project
By Doctus (kirikayuumura.noir@gmail.com)

Parse and execute chat commands.

    This file is part of RandomGameGenerator.

    RandomGameGenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RandomGameGenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with RandomGameGenerator.  If not, see <http://www.gnu.org/licenses/>.
'''
from libraries.rggSystem import fake, translate
from libraries.rggViews import say, generateName, localuser, rollDice, reportCamera, storeChat, releaseChat, incrementDreams, getDreams
from libraries.rggConstants import BASE_STRING, UNICODE_STRING, LATE_RESPONSE_LEVEL
from libraries.rggEvent import addChatInputListener
from libraries.rggRemote import sendSay, sendEmote, sendWhisper

chatCommands = {}
chatCommandNames = []

defaultDocumentation = fake.translate('chat', 'No documentation found.')

def chat(*args, **kwargs):
	"""Adds chat commands to the dict. (Decorator)"""
	def inner(func):
		assert(len(args) > 0)
		for arg in args:
			chatCommands[arg] = func
		if not kwargs.get('hidden'):
			chatCommandNames.append(args[0])
		func.documentation = defaultDocumentation
		return func
	return inner

def splitword(message):
	"""Split into a pair: word, rest."""
	words = message.split(None, 1)
	if not words:
		return '', ''
	rest = words[1] if len(words) > 1 else ''
	return words[0], rest

def squish(message):
	"""Squishes a message and converts it to lowercase."""
	return ''.join(message.split()).lower()

@chat('say', hidden=True)
def sayChat(message):
	sendSay(message)

sayChat.documentation = fake.translate('chatdoc',
	"""/say: Say a chat message. You do not need to write this as a command.<dl>
	<dt>Example:</dt>
		<dd>Hello there!</dd>
		<dd>/say Hello there!</dd>
	</dl><br>
	""")

@chat('generate')
def randomname(message):
	if len(message) <= 0:
		say(translate('chat',
			"Syntax: /generate NAMETYPE. For a list of available generators, see /generate keys. Use /generate help NAMETYPE for more information on a generator."))
	else:
		generateName(*splitword(message.lower()))

randomname.documentation = fake.translate('chatdoc',
	"""/randomname: This documentation is a lie!<dl>
	<dt>Syntax:</dt>
		<dd>/randomname NAMETYPE. Caps and spaces are ignored.</dd>

	<dt>Example:</dt>
		<dd>/randomname JAPANESEFEMALEFULL</dd>
		<dd>/randomname DwArF M aLe</dd>
	</dl><br>
	""")

@chat('roll')
def roll(message):
	if not message:
		dice = '2d6'
	else:
		dice = ' '.join(message.split())
	rollDice(dice)

roll.documentation = fake.translate('chatdoc',
	"""/roll: Roll the dice. The dice can be in the form of macros or
	like 3d8, for 3 dice with 8 sides. You can also add dice.
	Specify no dice to roll 2d6.<dl>
	<dt>Examples:</dt>
		<dd>/roll</dd>
		<dd>/roll 10d2</dd>
		<dd>/roll mydicemacro</dd>
		<dd>/roll d2 + d6 + 10d2</dd>
	</dl><br>
	""")

@chat('proll')
def proll(message):
	if not message:
		dice = '2d6'
	else:
		dice = ' '.join(message.split())
	rollDice(dice, True)

roll.documentation = fake.translate('chatdoc',
	"""/proll: Same as /roll but private.<br>
	""")

@chat('emote', 'me')
def emote(message):
	if not message:
		say(translate('chat', "Syntax: /me DOES ACTION. Displays '[HANDLE] DOES "
				"ACTION' in italic font."))
	else:
		sendEmote(message)

emote.documentation = fake.translate('chatdoc',
	"""Display an emote in italics.<dl>
	<dt>Alternate spelling:</dt>
		<dd>/techname</dd>

	<dt>Examples:</dt>
		<dd>/techiquename</dd>
		<dd>/techniquename ...</dd>
	</dl><br>
	""")

@chat('whisper', 'w', 't', 'tell', 'msg', 'message')
def whisper(message):
	if not message:
		say(translate('chat', "Syntax: /whisper HANDLE MESSAGE. Sends a message "
			"only to the specified user. Spaces MUST be correct."
			" Handle may be caps-sensitive."))
	else:
		target, rest = splitword(message)
		if target.lower() == localuser().username:
			emote(translate('chat', "mutters something."))
		elif not rest:
			say(translate('chat', "What do you want to tell {target}?").format(target=target))
		else:
			sendWhisper(target, rest)

whisper.documentation = fake.translate('chatdoc',
	"""/whisper: Whisper a message to another user.<dl>
	<dt>Alternate spellings:</dt>
		<dd>/w, /tell, /t, /message, /msg</dd>

	<dt>Syntax:</dt>
		<dd>/whisper NAME message</dd>

	<dt>Example:</dt>
		<dd>/tell danny HEEL PLZ</dd>
	</dl><br>
	""")

@chat('camera', 'cam')
def camera(message, hidden=True):
	reportCamera()

camera.documentation = fake.translate('chatdoc',
	"""camera: Display the current camera location.<dl>
	<dt>Alternate spelling:</dt>
		<dd>/cam</dd>
	</dl><br>
	""")

@chat('store', 'rumble', 'simultaneous')
def store(message):
	storeChat(message)

store.documentation = fake.translate('chatdoc',
	"""store: store message for simultaneous display.  Example: /store I defend against the goblin.<br>
	""")

@chat('release', 'display')
def store(message):
	releaseChat()

store.documentation = fake.translate('chatdoc',
	"""release: display stored simultaneous messages.<br>
	""")

@chat('dream', 'd', 'adddream')
def dream(message):
	message = message.split()
	target = message[0]
	try:
		amount = int(message[1])
	except:
		amount = 1
	incrementDreams(target, amount)

dream.documentation = fake.translate('chatdoc',
	"""dream: add dreams to a player.<br>
	""")

@chat('dreams')
def dreams(message):
	dr = getDreams()
	for user, amount in dr.items():
		say("%s: %s"%(user, BASE_STRING(amount)))

dreams.documentation = fake.translate('chatdoc',
	"""dreams: list current dream amounts.<br>
	""")

def chat(st):
	"""Parses and executes chat commands."""
	st = UNICODE_STRING(st)

	if (len(st) <= 0):
		return
	if ('<' in st and '>' not in st) or ('<' in st and '>' in st and '<' in st[st.rfind('>'):]):
		say(translate('chat', "Please type &#60; if you wish to include < in your message."))
		return

	if st[0] != '/' or len(st) > 1 and st[1] == '/':
		if len(st) > 1 and st[1] == '/':
			st = st[1:]
		command = 'say'
		message = st.strip()
	else:
		command, message = splitword(st[1:])
		command = UNICODE_STRING(command).lower()
	#print command, message

	if command in chatCommands:
		chatCommands[command](message)
	else:
		if command not in ('help', '?'):
			say(translate('chatdoc', "Invalid command.", 'Unknown chat command name.'))
		elif message in chatCommands:
			say(translate('chatdoc', chatCommands[message].documentation))
			return
		say(translate('chatdoc', "Command Help:<br>"
			"Typing ordinary text and pressing 'enter' "
			"will display to all players. Other commands may be invoked "
			"with '/' plus the name of the command plus any arguments."
			"<dl><dt>Commands</dt><dd>{commandList}</dd></dl><br>").format(
				commandList=translate('chatdoc',
					'</dd><dd>',
					'Goes inbetween the commands in the commandList.').
					join(chatCommandNames)))

addChatInputListener(chat, LATE_RESPONSE_LEVEL)

