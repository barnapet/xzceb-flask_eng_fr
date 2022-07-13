"""
A module for translating text from english to french,
and french to english.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2022-06-27',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
	English to french translator.
        Parameters:
		english_text (str): English text (what you want
		to translate)
        Returns:
		return french_text(str): Translated text. 
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    get_only_word = translation.get('translations')
    french_text = get_only_word[0].get('translation')
    print (french_text)
    return french_text

def french_to_english(french_text):
    '''
	French to english translator.
	Parameters:
		french_text (str): French text (what you want
		to translate)
	Returns:
		return english_text(str): Translated text.
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    get_only_text = translation.get('translations')
    english_text = get_only_text[0].get('translation')
    print (english_text)
    return english_text

#english_to_french("Yes")
#french_to_english("Tu me manques!")
