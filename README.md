Azure Language Understanding
============================

This [MLHub](https://mlhub.ai) package provides a quick demonstration
of the pre-built Language Understanding (LUIS) model provided through
Azure's Cognitive Services. This service takes a command as text
and parses it to return the intent and entities found in the command.

An Azure subscription is required and a free Azure subscription
allowing up to 5,000 transactions per month is available from
https://azure.microsoft.com/free/. Once set up visit and login to
https://luis.ai to obtain a subscription key, endpoint, location and 
App Id. This information will be added when running
```console
$ ml configure azlang
```

Please note that this is *closed source software* which limits your
freedoms and has no guarantee of ongoing availability.

Visit the github repository for more details:
<https://github.com/gjwgit/azlang>

The Python code is based on the [Language Understanding
Quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-get-started-python-get-intent).

## LUIS App
Through the [LUIS preview portal](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-get-started-create-app)
to create your first LUIS App. Once the App is published, in the *Manage* 
section (top-right menu), on the *Azure Resources* page (left menu), 
your Primary Key, endpoint and Location will be there. Your App ID will be 
on the *Settings* page. 

Usage
-----

MLHub is a command line utility to quickly demonstrate the
capabilities of pre-built machine learning models and data science
processes. Visit [MLHub.ai](https://mlhub.ai) for details.

To install and run the pre-built model:

    $ pip3 install mlhub
    $ ml install   azlang
    $ ml configure azlang
    $ ml demo      azlang

## Command Line Tools

In addition to the *demo* command below, the package provides a number
of useful command line tools.

### *intent*

The *intent* command will recognize what your wishes to initiate 
or do based on options you define in LUIS. 

Intent is something that users want to do: such as turn on the 
light, turn off the oven, check the weather. 

This command will listen for an intent from the computer microphone 
and then parses it to return the intent, score and entities found in 
the command.

```console
$ ml intent azlang
Recognized: "Turn on the oven." with intent id `HomeAutomation.TurnOn`. The score: 0.99811447, and the entities: oven
```

