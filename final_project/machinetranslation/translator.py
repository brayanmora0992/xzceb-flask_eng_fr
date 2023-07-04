"""Beginning"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """

    This function translates english text into french
    """

    translator = MyMemoryTranslator

    french_text = translator(source='english', target='french').translate(english_text)

    return french_text

def french_to_english(french_text):
    """

    This function translates french text into english
    """

    translator = MyMemoryTranslator

    english_text = translator(source='french', target='english').translate(french_text)

    return english_text
