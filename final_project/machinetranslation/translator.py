import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']


# Translator Instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


# Translate
def english_to_french(english_text):
    if english_text == '': return ''
    else:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        return french_text


def french_to_english(french_text):
    if french_text == '': return ''
    else:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        return english_text


# Print results
print(json.dumps(english_to_french("Hello"), indent=2, ensure_ascii=False))
print(json.dumps(french_to_english("Bonjour"), indent=2, ensure_ascii=False))
