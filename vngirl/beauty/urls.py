from django.urls import path, include
from .views import ImageList, ImageListAPI, ImageDetailAPI, RandomImageAPI


urlpatterns = [
    path('images', ImageListAPI.as_view()),
    path('images/random/', RandomImageAPI.as_view()),
    path('images/<int:pk>/', ImageDetailAPI.as_view()),
    # path('', ImageList.as_view()),
]
