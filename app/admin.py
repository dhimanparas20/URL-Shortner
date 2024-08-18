from django.contrib import admin
from .models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    search_fields = ['short_url','long_url']
    list_display = ['short_url','long_url']
    # list_filter = ['short_url','long_url']