import json
import requests
import re
import string
from myproject.settings_secret import token, botid
from foaas import fuck

def receive(message):
    if not_bot(message['sender_type']):
        content = message['text']

        if contains_chat_trigger(content):
            pattern = re.compile('([^\s\w]|_)+')
            content = pattern.sub('', content)
            print(content)

            args = content.split()

            if len(args) > 0:
                msg_to_send = get_return_message(args)
                boturl = 'https://api.groupme.com/v3/bots/post'
                headers = {'Content-Type': 'application/json'}

                response_from_groupme = requests.post(boturl, headers=headers, data=msg_to_send)

def get_return_message(args):
    message = '{"text":"'

    if args[0].lower() == 'help':
        message = message + 'Fuck you. There is no help.'

    elif args[0].lower() == 'trigger' or args[0].lower() == 'triggered':
        if len(args) == 1:
            message = message + 'TRIGGERED!'
        elif len(args) > 1:
            for index in range(1, len(args)):
                if index > 1:
                    message = message + ' '
                message = message + args[index].upper()
            message = message + ' IS TRIGGERED!'

    elif args[0].lower() == 'lel':
        if len(args) == 1:
            message = message + 'LEL'

    elif args[0].lower() == 'fuck':
        if len(args) == 1:
            foaasMessage = fuck.random(from_= ' ').text[:-3]
            message = message + foaasMessage
        elif len(args) == 2:
            foaasMessage = fuck.random(name=args[1].title(), from_= ' ').text[:-3]
            message = message + foaasMessage

    elif args[0].lower() == 'kek':
        if len(args) == 1:
            message = message + 'TOPKEK'

    elif args[0].lower() == 'flake':
        if len(args) > 1:
            for index in range(1, len(args)):
                if index > 1:
                    message = message + ' '
                message = message + args[index].upper()
            message = message + ' IS A FLAKE!'

    message = message + '","bot_id":"' + botid + '"}'
    print(message)
    return message


def contains_chat_trigger(content):
    if content.startswith('!'):
        return True
    else:
        return False


def not_bot(sender_type):
    if sender_type != 'bot':
        return True
    else:
        return False
