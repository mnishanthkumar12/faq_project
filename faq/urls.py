# faq/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/faqs/', views.get_faqs, name='get_faqs'),  # URL pattern for the FAQ API
]
