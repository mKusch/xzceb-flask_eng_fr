"""This is a fancy translator."""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """This is a function for translating english text to french."""
    french_text = MyMemoryTranslator('en', 'fr').translate(english_text)

    return french_text

def french_to_english(french_text):
    """This is a function for translating french text to english."""
    english_text = MyMemoryTranslator('fr', 'en').translate(french_text)

    return english_text
