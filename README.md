Azure Language Understanding
============================

This [MLHub](https://mlhub.ai) package provides a quick demonstration
of the pre-built Language Understanding (LUIS) model provided through
Azure's Cognitive Services. This service takes a command and parses it
to return the intent and entities.

An Azure subscription is required and a free Azure subscription
allowing up to 5,000 transactions per month is available from
https://azure.microsoft.com/free/. Once set up visit and login to
https://luis.ai to obtain a subscription key. The key will be prompted
for in the demo.

Please note that this is *closed source software* which limits your
freedoms and has no guarantee of ongoing availability.

Visit the github repository for more details:
<https://github.com/gjwgit/azlang>

The Python code is based on the [Language Understanding
Quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-get-started-python-get-intent)

Usage
-----

To install and run the pre-built model:

    $ pip3 install mlhub
    $ ml install   azlang
    $ ml configure azlang
    $ ml demo      azlang

