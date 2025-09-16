from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer
from utils import ResponseMessage


# Create your views here.
class CommentGenericAPIView(ViewSetMixin,
                            GenericAPIView,
                            ListModelMixin,
                            CreateModelMixin,
                            RetrieveModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin
                            ):
    queryset = Comment.objects
    serializer_class = CommentSerializer

    def single(self,request,pk):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        print("我是查询一个")
        return self.retrieve(request,pk)

    def my_list(self,request):
        print("我是查询多个")
        return self.list(request)

    def edit(self,request,pk):
        print("我是更新")
        return self.update(request,pk)

    def my_save(self,request):
        print("我是保存")
        return self.create(request)

    def my_delete(self,request,pk):
        print("我是删除")
        return self.destroy(request,pk)

class CommentAPIView(APIView):
    def get(self,request):
        sku_id=request.GET.get("sku_id")
        page=request.GET.get("page")
        start=(int(page)-1)*15
        end=int(page)*15
        db_result=Comment.objects.filter(sku_id=sku_id).all()[start:end]
        ser_data = CommentSerializer(instance=db_result,many=True)
        # return JsonResponse()
        return ResponseMessage.CommentResponse.success(ser_data.data)

class CommentCountAPIView(APIView):
    def get(self,request):
        sku_id=request.GET.get("sku_id")
        db_result = Comment.objects.filter(sku_id=sku_id).count()
        return Response(db_result)

