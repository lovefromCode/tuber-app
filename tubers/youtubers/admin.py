from django.contrib import admin
from . import models
from django.utils.html import format_html


class YtAdmin(admin.ModelAdmin):

    def pics(self, object):
        return format_html('<img src="{}" width= "40" />'.format(object.photo.url))

    list_display = ('id', 'pics', 'name', 'subs_count', 'is_featured')
    list_display_links = ('id', 'name')
    list_filter = ('city', 'camera_type',)
    search_fields = ('name', 'camera_type')
    list_editable = ('is_featured',)


admin.site.register(models.Youtuber, YtAdmin)
