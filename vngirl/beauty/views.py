from django.views.generic import ListView
from rest_framework import generics

from .models import Image
from .serializers import ImageSerializer


QS = Image.objects.order_by('-posted_date')


class ImageList(ListView):
    model = Image
    context_object_name = 'images'


class ImageListAPI(generics.ListAPIView):
    queryset = QS
    serializer_class = ImageSerializer


class ImageDetailAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
