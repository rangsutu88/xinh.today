from random import randint
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer


QS = Image.objects.order_by('-posted_date')


def get_random_image():
    count = Image.objects.count()
    random_image = Image.objects.all()[randint(0, count - 1)]
    return random_image


class ImageList(ListView):
    model = Image
    context_object_name = 'images'


class ImageListAPI(generics.ListAPIView):
    queryset = QS
    serializer_class = ImageSerializer


class ImageDetailAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RandomImageAPI(APIView):
    def get(self, request):
        image = get_random_image()
        serializer = ImageSerializer(image)
        return Response(serializer.data)
