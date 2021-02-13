from django.contrib import admin
from . import models
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def func1(self, object):
        return format_html('<img src="{}" width= "40" />'.format(object.photo.url))

    list_display = ('id', 'first_name', 'func1', 'role', 'created_at')
    list_display_links = ('id', 'first_name')
    list_filter = ('first_name', 'role',)
    search_fields = ('first_name', 'role')


class SliderAdmin(admin.ModelAdmin):

    def pics(self, object):
        return format_html('<img src="{}" width= "230" />'.format(object.photo.url))

    list_display = ['subtitle', 'pics', 'button_text', 'created_at']
    list_display_links = ('subtitle',)
    list_filter = ('subtitle', 'button_text',)


admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.About)
