import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.menu.models import MainMenu, SubMenu
from utils import ResponseMessage


# Create your views here.
class GoodsMainMenu(View):
    def get(self,request):
        print("get请求来啦")
        main_menu = MainMenu.objects.all()
        result_list = []
        # result_json = {}
        for m in main_menu:
            # result_list.append(m)
            result_list.append(m.__str__())

        return ResponseMessage.MenuResponse.success(result_list)
        # {status:1000,data:result_list}
        # result_json["status"] = 1000
        # result_json["data"] = result_list
        # return HttpResponse(json.dumps(result_json),content_type="application/json")
        # return HttpResponse(result_list)
        # return HttpResponse("get请求")

    def post(self,request):
        print("post请求来啦")
        return HttpResponse("post请求")

class GoodsSubMenu(View):
    def get(self,request):
        # 获取请求的参数
        param_id = request.GET["main_menu_id"]
        # 拿到二级菜单的内容
        sub_menu = SubMenu.objects.filter(main_menu_id=param_id)
        result_list = []
        # result_json = {}
        for m in sub_menu:
            # result_list.append(m)
            result_list.append(m.__str__())
        # {status:1000,data:result_list}
        # result_json["status"] = 1000
        # result_json["data"] = result_list
        return ResponseMessage.MenuResponse.success(result_list)
        # return HttpResponse(json.dumps(result_json), content_type="application/json")

