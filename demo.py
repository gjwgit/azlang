# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Azure Cognitive Services Text Analytics Quick Starts
# 
# https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python


print("""============================
Azure Language Understanding
============================

Welcome to a demo of LUIS, a language understanding module provided
through Azure's Cognitive Services. This service takes a command string
and returns an understanding of the intent of the command in the form of
an operation to be performed on specific entities.
""")

# Defaults.

KEY_FILE = "private.py"
DEFAULT_REGION = "southeastasia"
CANNED_PKL = "canned.pkl"

fname = KEY_FILE
region = DEFAULT_REGION
subscription_key = None
live = True

# Import the required libraries.

import sys
import os
import requests
import pickle
from time import sleep

# Prompt the user for the key region and region, and to save into
# private.py for future runs of the model. The contents of that file
# is:
#
# subscription_key = "a14d...ef24"
# region = "southeastasia"

fname = "private.py"

if os.path.isfile(fname):
    sys.stdout.write("""The following file has been found and is assumed to contain an Azure
LUIS subscription key and region. We will load the file and use this
information.

{}
""".format(os.getcwd() + "/" + fname))
    exec(open(fname).read())
else:
    sys.stdout.write("""An Azure resource is required to access this service (and to run this
demo). See the README for details of a free subscription. Then you can
provide the key and the region information here.

If you don't have a key and want to review the canned examples rather
than work with the live examples, you can indeed continue simply by 
pressing the Enter key.
""")
    sys.stdout.write("Please enter your LUIS subscription key []: ")
    subscription_key = input()

    sys.stdout.write("Please enter your region [southeastasia]: ")
    region = input()
    if len(region) == 0: region = DEFAULT_REGION

    if len(subscription_key) > 0:
        assert subscription_key
        ofname = open(fname, "w")
        ofname.write("""subscription_key = "{}"
region = "{}"
    """.format(subscription_key, region))
        ofname.close()

        sys.stdout.write("""
I've saved that information into the file:

""" + os.getcwd() + "/" + fname)

# Handle canned demonstration.
    
if len(subscription_key) == 0:
    live = False
    with open(CANNED_PKL, 'rb') as f:
        commands, responses = pickle.load(f)
    sys.stdout.write("""
No subscription key was provided so we will continue with a canned
demonstration. The analyses from the cloud through the API have previously
been captured and so we will use them.
""")
    
sys.stdout.write("""
Press Enter to continue: """)
answer = input()

# Build the URL request headers.

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

sys.stdout.write("""
LUIS includes a set of prebuilt intents from a number of prebuilt domains
for quickly adding common intents and utterances to conversational client
apps. These include Camera, Music, HomeAutomation, and many more. We will
begin with a demonstration of Home Automation. Do note that typically you
will need to train the LUIS model with your speceific intents.

Below we will demonstrate a series of commands and identify the intent and
the entities, together with a confidence score.

Press Enter to continue: """)
answer = input()

if live:
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

url = ('https://{}.api.cognitive.microsoft.com/luis/v2.0/apps/' +
       'df67dcdb-c37d-46af-88e1-8b97951ca1c2').format(region)

for command in commands:
    params ={
        # Query parameter
        'q': command,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        if live:
            r = requests.get(url, headers=headers, params=params)
            rj = r.json()
            responses[command] = rj
        else:
            rj = responses[command]
        qr = rj['query']
        intent = rj['topScoringIntent']
        entities = ""
        sep = ""
        for e in rj['entities']:
            entities += sep + e['entity']
            sep = ", "
        
        sys.stdout.write("""
Command: {}
  Intent: {} score {:.2f}
  Entities: {}
""".format(rj['query'], intent['intent'], intent['score'], entities))
    
    except Exception as e:
        sys.stderr.write("[Errno {0}] {1}".format(e.errno, e.strerror))

    sleep(0.2) # Limit of 5 queries per second so sleep between each

# This is how we save the responses for the canned demonstration.
# If the documents above change we need a new can of pickles.

if False:
    with open(CANNED_PKL, 'wb') as f:
        pickle.dump([commands, responses], f)
