from django.urls import path, include
from .views import ImageList, ImageListAPI, ImageDetailAPI


urlpatterns = [
    path('images', ImageListAPI.as_view()),
    path('images/<int:pk>/', ImageDetailAPI.as_view()),
    # path('', ImageList.as_view()),
]
