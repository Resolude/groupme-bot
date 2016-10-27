import json
import random
import requests

from myproject.settings_secret import token, botid
from foaas import fuck
import triggers
import urls

headers = {'Content-Type': 'application/json'}


def receive(message):
    message_json = json.loads(message)
    if not_bot(message_json['sender_type']):
        content = message_json['text']

        if (triggers.has_trigger(content)
                and (content.startswith(triggers.command_sequence)
                     or random.randint(0, 100) < 25)):
            try:
                data = triggers.get_response(content)
                data["bot_id"] = botid
                print(data)
                requests.post(urls.bot_url, headers=headers, data=data)
            except ValueError:
                pass


def not_bot(sender_type):
    if sender_type != 'bot':
        return True
    else:
        return False
