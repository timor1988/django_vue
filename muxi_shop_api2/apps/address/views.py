from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin

from apps.address.models import UserAddress
from apps.address.serializers import AddressSerializer
from utils import ResponseMessage
from utils.jwt_auth import JwtQueryParamAuthentication, JwtHeaderAuthentication


# Create your views here.
class AddressGenericAPIView(GenericAPIView,
                            CreateModelMixin,
                            RetrieveModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer
    authentication_classes = [JwtHeaderAuthentication,]

    def post(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        email = request.user.get("data").get("username")
        request_data = request.data
        request_data["email"] = email
        if request_data["default"] == True:
        #     如果这个值是true，那么这个地址就是默认地址，我需要把所有地址先改成0
            self.get_queryset().filter(email=email).update(default=0)
            request_data["default"] = 1
        else:
            request_data["default"] = 0
        self.get_queryset().create(**request_data)

        return ResponseMessage.AddressResponse.success("OK")
        # return self.create(request)

    # 返回全部地址
    def get(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email = request.user.get("data").get("username")
        db_result = self.get_queryset().filter(email=email).all().order_by("-default","create_time")
        ser = self.get_serializer(instance=db_result,many=True)
        return ResponseMessage.AddressResponse.success(ser.data)
        # return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

class AddressListGenericAPIView(GenericAPIView,ListModelMixin):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer
    authentication_classes = [JwtQueryParamAuthentication,]
    def get(self,request):
        # 拿到token验证返回的第一个值
        print(request.user)
        # 拿到token返回的第二个值
        print(request.auth)
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)

        return self.list(request)

class UserAddressDetailGenericAPIView(GenericAPIView,ListModelMixin,
                                CreateModelMixin,
                                RetrieveModelMixin,
                                UpdateModelMixin,
                                DestroyModelMixin
                                ):
    queryset = UserAddress.objects
    serializer_class = AddressSerializer

    def post(self, request):
        if not request.user.get("status"):
            return JsonResponse(request.user, safe=False)
        email = request.user.get("data").get("username")
        request_data = request.data
        request_data["email"] = email
        if request_data["default"] == True:
            #     如果这个值是true，那么这个地址就是默认地址，我需要把所有地址先改成0
            self.get_queryset().filter(email=email).update(default=0)
            request_data["default"] = 1
        else:
            request_data["default"] = 0
        self.get_queryset().filter(id=request_data["id"]).update(**request_data)

        return ResponseMessage.AddressResponse.success("OK")
