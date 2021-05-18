# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com

from mlhub.pkg import mlask, mlcat
mlcat('Azure Language Understanding', """\
Welcome to a demo of LUIS, a language understanding module provided
through Azure's Cognitive Services. This service takes a command string
and returns an understanding of the intent of the command in the form of
an operation to be performed on specific entities.
""")

mlask(end="\n")

# Import the required libraries.

import sys
import requests
from time import sleep
from utils import request_priv_info

# ----------------------------------------------------------------------
# Request subscription key, endpoint and App ID from user.
# ----------------------------------------------------------------------
subscription_key, endpoint, id = request_priv_info()



mlcat("", """"\
LUIS includes a set of prebuilt intents from a number of prebuilt domains
for quickly adding common intents and utterances to conversational client
apps. These include Camera, Music, HomeAutomation, and many more. We will
begin with a demonstration of Home Automation. Do note that typically you
will need to train the LUIS model with your speceific intents.

Below we will demonstrate a series of commands and identify the intent and
the entities, together with a confidence score.
""")
mlask()

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

responses = {}
commands = ['Turn off the lights',
                'Stop the coffee maker',
                'Open the garage door',
                'Turn off the living room light',
                'Turn off the living room heater',
                'Can you turn on my coffee maker?',
                'Set the thermostat to 72 degrees.',
                'Close the bedroom door',
                'Turn on the kitchen lights'
]


url = f'{endpoint}luis/prediction/v3.0/apps/{id}/production/predict'


for command in commands:
    params = {
        'query': command,
        'timezoneOffset': '0',
        'verbose': 'true',
        'show-all-intents': 'true',
        'spellCheck': 'false',
        'staging': 'false',
        'subscription-key': subscription_key
    }

    try:
        r = requests.get(url, headers=headers, params=params)
        rj = r.json()
        responses[command] = rj

        qr = rj['query']
        intent = rj['prediction']['topIntent']
        entities = ""
        sep = ""

        for e in rj['prediction']['entities']:
            if e != "$instance":
                entities += sep + e+"-"+''.join(rj['prediction']['entities'][e][0])
                sep = ", "

        sys.stdout.write("""
    Command: {}
      Intent: {} score {:.2f}
      Entities: {}
    """.format(qr, intent, rj['prediction']['intents'][intent]['score'], entities))

    except Exception as e:
        sys.exit(e)

    sleep(0.2) # Limit of 5 queries per second so sleep between each
