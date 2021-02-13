from django.contrib import admin
from .models import Hiretuber


class HireYtAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'tuber_name', 'email')
    list_display_links = ('first_name',)
    list_filter = ('email', 'tuber_name',)
    search_fields = ('city', 'tuber_name')


admin.site.register(Hiretuber, HireYtAdmin)
