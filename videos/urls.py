from django.http import HttpResponse
from django.urls import path
from .views import *

urlpatterns = [
    path('', VideosView.as_view()),
]
