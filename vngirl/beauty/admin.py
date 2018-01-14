from django.contrib import admin
from django.utils.html import format_html
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="height: auto; width: 30%;" />'.format(obj.url))

    list_display = ('image_tag', 'url', 'file_size', 'posted_date', 'created_at')


admin.site.register(Image, ImageAdmin)
