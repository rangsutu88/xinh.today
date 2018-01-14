from django.db.models import (
    Model, CharField, URLField, DateTimeField, SmallIntegerField
)


class Image(Model):
    source = URLField(max_length=255)
    url = URLField(max_length=255, null=True)
    file_size = SmallIntegerField(null=True)
    point = SmallIntegerField(default=5)
    posted_date = DateTimeField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
