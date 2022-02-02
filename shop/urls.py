from django.urls import path

from .views import *


urlpatterns = [
    path('shop/', ShopList.as_view()),
    path('shop/<str:pk>', ShopDetail.as_view()),
]
