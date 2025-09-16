

from django.urls import path, re_path
from .views import OrderGoodsGenericAPIView,OrderGenericAPIView,OrderDetailGenericAPIView

urlpatterns = [
    path("",OrderGenericAPIView.as_view()),
    path("goods/",OrderGoodsGenericAPIView.as_view()),
    path("update/",OrderDetailGenericAPIView.as_view()),
    re_path("goods/(?P<trade_no>.*)",OrderGoodsGenericAPIView.as_view()),
]

