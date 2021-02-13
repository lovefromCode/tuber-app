from django.contrib import admin
from .models import Contact_tuber


class ContactYtAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'email']
    list_display_links = ('full_name',)
    list_filter = ('full_name', 'subject',)
    search_fields = ('city', 'tuber_name')


admin.site.register(Contact_tuber, ContactYtAdmin)
