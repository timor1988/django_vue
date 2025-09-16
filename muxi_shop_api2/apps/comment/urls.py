

from django.urls import path, re_path
from .views import CommentGenericAPIView,CommentAPIView,CommentCountAPIView

urlpatterns = [
    # path("",CommentGenericAPIView.as_view({
    #     "get":"my_list",
    #     "post":"my_save"
    # })),
    # re_path("(?P<pk>.*)",CommentGenericAPIView.as_view(
    #     {
    #         "get":"single",
    #         "post":"edit",
    #         "delete":"my_delete"
    #     }
    # )),
    path("detail", CommentAPIView.as_view()),
    path("count", CommentCountAPIView.as_view()),
]


