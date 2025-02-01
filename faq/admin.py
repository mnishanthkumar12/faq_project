from django.contrib import admin

# Register your models here.
# faq/admin.py

from django.contrib import admin
from .models import FAQ

# Register your models here.
admin.site.register(FAQ)
