

from django.urls import path, re_path
from .views import AddressGenericAPIView,AddressListGenericAPIView,UserAddressDetailGenericAPIView

urlpatterns = [
    path("",AddressGenericAPIView.as_view()),
    path("edit",UserAddressDetailGenericAPIView.as_view()),
    path("list",AddressListGenericAPIView.as_view()),
    re_path("(?P<pk>.*)",AddressGenericAPIView.as_view()),
]

