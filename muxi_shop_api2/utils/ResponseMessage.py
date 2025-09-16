import json

from django.http import HttpResponse, JsonResponse


# 我们的菜单成功了状态码就是1000
# 失败了就是1001
# 其它不确定的1002
class MenuResponse():

    @staticmethod
    def success(data):
        result = {"status":1000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")

    @staticmethod
    def failed(data):
        result = {"status": 1001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 1002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")
# 商品的响应全部都是2开头的
class GoodsResponse():

    @staticmethod
    def success(data):
        result = {"status":2000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")

    @staticmethod
    def failed(data):
        result = {"status": 2001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 2002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")


# 购物车的响应全部都是3开头的
class CartResponse():

    @staticmethod
    def success(data):
        result = {"status":3000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 3001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 3002, "data": data}
        return JsonResponse(result, safe=False)


# 用户的响应全部都是4开头的
class UserResponse():

    @staticmethod
    def success(data):
        result = {"status":4000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 4001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 4002, "data": data}
        return JsonResponse(result, safe=False)


# 评论的响应全部都是5开头的
class CommentResponse():

    @staticmethod
    def success(data):
        result = {"status":5000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 5001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 5002, "data": data}
        return JsonResponse(result, safe=False)



# 订单的响应全部都是6开头的
class OrderResponse():

    @staticmethod
    def success(data):
        result = {"status":6000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 6001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 6002, "data": data}
        return JsonResponse(result, safe=False)


# 地址的响应全部都是7开头的
class AddressResponse():

    @staticmethod
    def success(data):
        result = {"status":7000,"data":data}
        return JsonResponse(result,safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 7001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 7002, "data": data}
        return JsonResponse(result, safe=False)