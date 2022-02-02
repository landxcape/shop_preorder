from django.urls import path

from .views import *


urlpatterns = [
    path('order/', OrderList.as_view()),
    path('order/<str:pk>', OrderDetail.as_view()),
]
