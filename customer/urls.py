from django.urls import path

from .views import *


urlpatterns = [
    path('customer/', CustomerList.as_view()),
    path('customer/<str:pk>', CustomerDetail.as_view()),
]
