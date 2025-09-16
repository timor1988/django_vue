from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializers import UserSerializer
from utils import ResponseMessage
from utils.jwt_auth import create_token
from utils.password_encode import get_md5


# Create your views here.
class UserApiView(APIView):
    # 注册功能的实现
    # def post(self,request):
    #     request.data["password"] = get_md5(request.data.get("password"))
    #     # 反序列化呀，把json变成一个对象  [这是关键的一句话]
    #     user_data_serializer = UserSerializer(data=request.data)
    #     user_data_serializer.is_valid(raise_exception=True)
    #     user_data = User.objects.create(**user_data_serializer.data)
    #
    #     # 序列化一下，把json返回给前端对象
    #     user_ser = UserSerializer(instance=user_data)
    #     return JsonResponse(user_ser.data)
    def post(self,request):
        # 反序列化呀，把json变成一个对象  [这是关键的一句话]
        user_data_serializer = UserSerializer(data=request.data)
        user_data_serializer.is_valid(raise_exception=True)
        user_data = user_data_serializer.save()

        # 序列化一下，把json返回给前端对象
        user_ser = UserSerializer(instance=user_data)
        # return JsonResponse(user_ser.data)
        return ResponseMessage.UserResponse.success(user_ser.data)

    def get(self, request):
        email = request.GET.get("email")
        try:
            user_data = User.objects.get(email=email)
            user_ser = UserSerializer(user_data)
            return ResponseMessage.UserResponse.success(user_ser.data)
        except Exception as e:
            print(e)
            return ResponseMessage.UserResponse.failed("用户信息获取失败")

class LoginView(GenericAPIView):
    def post(self,request):
        return_data = {}
        request_data = request.data
        email = request_data.get("username")
        try:
            user_data = User.objects.get(email=email)
        except Exception:
            return ResponseMessage.UserResponse.other("用户名或者是密码错误1")
        if not user_data:
            return ResponseMessage.UserResponse.other("用户名或者是密码错误1")
        else:
            user_ser = UserSerializer(instance=user_data,many=False)
            # 用户输入的密码
            user_password = request_data.get("password")
            md5_user_password = get_md5(user_password)
            print(md5_user_password)
            # 数据库的密码
            db_user_password = user_ser.data.get("password")
            print(db_user_password)
            if md5_user_password != db_user_password:
                return ResponseMessage.UserResponse.other("用户名或者是密码错误2")
            else:
                token_info = {
                    "username":email
                }
                token_data = create_token(token_info)
                return_data["token"] = token_data
                return_data["username"] = user_ser.data.get("name")
                return ResponseMessage.UserResponse.success(return_data)






