from googletrans import Translator

translator = Translator()

# Test translation from English to Hindi
translation = translator.translate('Flask is a lightweight framework of Python', src='en', dest='hi')
print(translation.text)
