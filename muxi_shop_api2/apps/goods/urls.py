

from django.urls import path
from .views import GoodsCategoryAPIView,GoodsDetailAPIView,GoodsFindAPIView,GoodsSearchAPIView,GoodsSearchDataCountAPIView

urlpatterns = [
    path("find", GoodsFindAPIView.as_view()),
    path("category/<int:category_id>/<int:page>",GoodsCategoryAPIView.as_view()),
    path("search/<str:keyword>/<int:page>/<int:order_by>",GoodsSearchAPIView.as_view()),
    path("<str:sku_id>",GoodsDetailAPIView.as_view()),
    path("get_keyword_data_count/<str:keyword>",GoodsSearchDataCountAPIView.as_view()),
]



