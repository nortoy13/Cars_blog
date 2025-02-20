from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'get_html_photo', 'slug')
    list_display_links = ('id', 'model')
    search_fields = ('brand', 'model')
    prepopulated_fields = {'slug': ('model',)}
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

admin.site.register(CarsModel, CarsModelAdmin)
admin.site.register(Category)