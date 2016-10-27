import json
import random
import re

import requests

from myproject.settings_secret import token, botid
from foaas import fuck
from . import triggers

headers = {'Content-Type': 'application/json'}


def receive(message_json):
    # Determine if incoming message is from a bot
    if not_bot(message_json['sender_type']):
        content = message_json['text']

        # If the message has a trigger, and either starts with the command sequence or it passes RNG
        if (triggers.has_trigger(content)
                and (content.startswith(triggers.command_sequence)
                     or random.randint(0, 100) < 25)):

            # Delete characters that aren't alphanumeric or spaces, also deletes chat trigger
            pattern = re.compile('([^\s\w]|_)+')
            content = pattern.sub('', content)
            print(content)

            try:
                # try and get the bot response
                data = triggers.get_response(content)
                data["bot_id"] = botid
                print(data)

                # post the response
                requests.post('https://api.groupme.com/v3/bots/post', headers=headers, data=data)
            except ValueError:
                pass


def not_bot(sender_type):
    if sender_type != 'bot':
        return True
    else:
        return False
