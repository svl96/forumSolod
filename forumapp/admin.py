from django.contrib import admin
from .models import Sections, Themes, Comments
# Register your models here.


class SectionsAdmin(admin.ModelAdmin):
    fields = ['sections_title']

admin.site.register(Sections, SectionsAdmin)
admin.site.register(Themes)
admin.site.register(Comments)
