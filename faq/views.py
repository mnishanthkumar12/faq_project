# import html
# from django.shortcuts import render

# # Create your views here.
# # views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import FAQ

# from django.utils.html import strip_tags

# @api_view(['GET'])
# def get_faqs(request):
#     """
#     Fetch FAQs in the selected language (default to English if no language is provided).
#     """
#     lang = request.GET.get('lang', 'en')  # Default to English if no language specified
#     faqs = FAQ.objects.all()  # Retrieve all FAQs from the database
#     faqs_data = []

#     for faq in faqs:
#         translated_question = faq.get_translated_question(lang)  # Get translated question

#         # Ensure 'faq.answer' exists and is a valid field
#         if faq.answer:
#             decoded_answer = html.unescape(faq.answer)
#         else:
#             decoded_answer = ""

#         faqs_data.append({
#             'question': translated_question,  # Translated question
#             'answer': decoded_answer,  # The answer is decoded
#         })

#     return Response(faqs_data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator  # Import googletrans for translation
from .models import FAQ

@api_view(['GET'])
def get_faqs(request):
    """
    Fetch FAQs in the selected language (default to English if no language is provided).
    """
    lang = request.GET.get('lang', 'en')  # Default to English if no language specified
    faqs = FAQ.objects.all()  # Retrieve all FAQs from the database
    faqs_data = []

    translator = Translator()  # Initialize googletrans Translator

    for faq in faqs:
        translated_question = translator.translate(faq.question, src='en', dest=lang).text  # Translate directly here
        faqs_data.append({
            'question': translated_question,  # Translated question
            'answer': faq.answer,  # The answer doesn't need translation (WYSIWYG content)
        })

    return Response(faqs_data, status=status.HTTP_200_OK)
