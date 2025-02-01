# # models.py

from django.db import models
# from django.core.cache import cache
from ckeditor.fields import RichTextField

# class FAQ(models.Model):
#     question = models.TextField()
#     answer = RichTextField()  # WYSIWYG support for answers
#     question_hi = models.TextField(null=True, blank=True)  # Hindi translation
#     question_bn = models.TextField(null=True, blank=True)  # Bengali translation

#     def get_translated_question(self, lang='en'):
#         """
#         Fetches the translated question. Caches the result for faster access.
#         """
#         cache_key = f"faq_{self.id}_question_{lang}"

#         # Try to get the cached translation
#         translated_question = cache.get(cache_key)

#         if not translated_question:
#             # If not cached, use the default or fall back to English
#             if lang == 'hi':
#                 translated_question = self.question_hi or self.question
#             elif lang == 'bn':
#                 translated_question = self.question_bn or self.question
#             else:
#                 translated_question = self.question  # Default to English

#             # Cache the result for 1 hour (60 minutes)
#             cache.set(cache_key, translated_question, timeout=3600)

#         return translated_question

#     def __str__(self):
#         return self.question



import requests
from django.core.cache import cache

# class FAQ(models.Model):
#     # your fields here
#     question = models.TextField()
#     answer = RichTextField()  # WYSIWYG support for answerngali translation

#     def get_translated_question(self, lang='en'):
#         """
#         Fetches the translated question. Caches the result for faster access.
#         If the translation is not found in the model, we fetch from a translation API.
#         """
#         cache_key = f"faq_{self.id}_question_{lang}"
#         translated_question = cache.get(cache_key)

#         if not translated_question:
#             translated_question = self.question  # Default to English
#             # Cache the translated question for 1 hour (60 minutes)
#             cache.set(cache_key, translated_question, timeout=3600)

#         return translated_question

#     def translate_text(self, text, target_lang):
#         """
#         Calls the LibreTranslate API to translate the given text into the target language.
#         """
#         url = "https://libretranslate.com/translate"
#         payload = {
#             "q": text,
#             "source": "en",  # Assuming English as the source language
#             "target": target_lang,
#             "format": "text"
#         }
#         response = requests.post(url, data=payload)
        
#         if response.status_code == 200:
#             return response.json().get("translatedText", text)
#         else:
#             return text  # If API fails, return the original text


import logging
from googletrans import Translator  # Import the Translator class from googletrans
from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache  # Cache to avoid repeated API calls

logger = logging.getLogger(__name__)

class FAQ(models.Model):
    question = models.TextField()  # Original question in English
    answer = RichTextField()  # WYSIWYG support for answers

    def translate_text(self, text, target_lang):
        """
        Uses googletrans to translate the given text into the target language.
        """
        translator = Translator()

        try:
            # Translate text using googletrans API
            translated = translator.translate(text, src='en', dest=target_lang)
            logger.info(f"Translation Success: {translated.text}")
            return translated.text
        except Exception as e:
            logger.error(f"Error in translation: {e}")
            return text  # Return the original text if translation fails

    def get_translated_question(self, lang='en'):
        """
        Fetches the translated question. Caches the result for faster access.
        """
        cache_key = f"faq_{self.id}_question_{lang}"

        # Try to get the cached translation
        translated_question = cache.get(cache_key)

        if not translated_question:
            # If not cached, use the translation method
            translated_question = self.translate_text(self.question, lang)

            # Cache the result for 1 hour (60 minutes)
            cache.set(cache_key, translated_question, timeout=3600)

        return translated_question

    def __str__(self):
        return self.question
