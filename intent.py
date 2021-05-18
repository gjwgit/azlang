import azure.cognitiveservices.speech as speechsdk
from utils import request_priv_info
import sys
import json


def intent(intent_conf, app_id):
    # ----------------------------------------------------------------------
    # Set up the intent recognizer
    # ----------------------------------------------------------------------

    intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_conf)

    id = app_id

    # ----------------------------------------------------------------------
    # set up the intents that are to be recognized. These can be a mix of simple
    # phrases and intents specified through a LanguageUnderstanding Model.
    # Here, we include all the intents.
    # ----------------------------------------------------------------------

    model = speechsdk.intent.LanguageUnderstandingModel(app_id=id)

    try:
        intent_recognizer.add_all_intents(model)
    except:
        print("Error: wrong App ID.", file=sys.stderr)
        sys.exit(1)

    # ----------------------------------------------------------------------
    # Starts intent recognition, and returns after a single utterance is recognized.
    # The end of a single utterance is determined by listening for silence at
    # the end or until a maximum of 15 seconds of audio is processed. It returns
    # the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable
    # only for single shot recognition like command or query.
    # ----------------------------------------------------------------------

    print("Please say one intent, such as turn off the light.")

    intent_result = intent_recognizer.recognize_once()

    if intent_result.reason == speechsdk.ResultReason.RecognizedIntent:
        js = intent_result.intent_json
        js = json.loads(js)
        print(js["topScoringIntent"])
        score = js["topScoringIntent"]["score"]
        entities = ""
        sep = ""
        for item in js["entities"]:
            entities += sep + item["entity"]
            sep = ", "

        print("Recognized: \"{}\" with intent id `{}`. The score: {}, and the entities: {}".
              format(intent_result.text, intent_result.intent_id, str(score), entities))
    elif intent_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(intent_result.text))
    elif intent_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(intent_result.no_match_details))
    elif intent_result.reason == speechsdk.ResultReason.Canceled:
        print("Intent recognition canceled: {}".format(intent_result.cancellation_details.reason))
        if intent_result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(intent_result.cancellation_details.error_details))


if __name__ == "__main__":
    # ----------------------------------------------------------------------
    # Request subscription key and location from user.
    # ----------------------------------------------------------------------

    key, location, app_id, location = request_priv_info()

    intent_config = speechsdk.SpeechConfig(subscription=key, region=location)
    intent(intent_config, app_id)
