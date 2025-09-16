from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView

from apps.cart.models import Cart
from apps.order.models import OrderGoods, Order
from apps.order.serializers import OrderGoodsSerializer, OrderSerializer, OrderManyGoodsSerializer
from utils import ResponseMessage

# Create your views here.
class OrderGoodsGenericAPIView(GenericAPIView):
    queryset = OrderGoods.objects
    serializer_class = OrderGoodsSerializer

    def post(self, request):
        # trade_no = request.data.get("trade_no")
        # print(self.get_queryset())
        # print(self.get_serializer())
        print(request.data)
        ser = self.get_serializer(data=request.data)
        ser.is_valid()
        ser.save()
        return JsonResponse("ok",safe=False)

    lookup_field = "trade_no"
    # def get(self, request,trade_no):
    #     # 这一行代码就实现了数据库里所有数据的查询
    #     # return JsonResponse(self.get_serializer(instance=self.get_queryset(),many=True).data,safe=False)
    #     print(trade_no)
    #     ser = self.get_serializer(instance=self.get_object(),many=False)
    #     # ser = self.get_serializer(instance=self.get_object(),many=True)
    #     return JsonResponse(ser.data,safe=False)
    def get(self,request,trade_no):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        email = request.user.get("data").get("username")

        db_result = Order.objects.filter(
            email=email,is_delete=0,trade_no=trade_no
        ).first()
        # 序列化数据
        order_ser = OrderManyGoodsSerializer(instance=db_result)
        return ResponseMessage.OrderResponse.success(order_ser.data)



class OrderGenericAPIView(GenericAPIView):
    queryset = Order.objects
    serializer_class = OrderSerializer

    def post(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        print(request.user)
        email = request.user.get("data").get("username")
#         生成订单号
        import time
        trade_no = int(time.time()*1000)
        request_data = request.data
        trade_data = request_data["trade"]
        goods_data = request_data["goods"]
        trade_data["trade_no"] = trade_no
        trade_data["email"] = email
        # 新创建的订单，支付状态就是0
        trade_data["pay_status"] = 0
        # 0就代表着未删除
        trade_data["is_delete"] = 0
        trade_data["create_time"] = datetime.now()

        serializer = self.get_serializer(data=trade_data)
        serializer.is_valid()
        serializer.save()
        goods_order_data={}
        for data in goods_data:
            goods_order_data["trade_no"] = trade_no
            goods_order_data["sku_id"] = data["sku_id"]
            goods_order_data["goods_num"] = data.get("nums")
            if goods_order_data["goods_num"] is None:
                goods_order_data["goods_num"] = data.get("goods_nums")
            OrderGoods.objects.create(**goods_order_data)
#             把这个商品从购物车中删除
            Cart.objects.filter(sku_id=data["sku_id"],email=trade_data["email"]).update(is_delete=1)
        return ResponseMessage.OrderResponse.success(serializer.data)

    def get(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        email = request.user.get("data").get("username")
        # email="4@qq.com"
        pay_status = request.GET.get("pay_status")
        print(pay_status)
        if pay_status == "-1":
            db_result = Order.objects.filter(
                email=email,is_delete=0
            ).all().order_by("-create_time")
        else:
            db_result = Order.objects.filter(
                email=email, is_delete=0,pay_status=pay_status
            ).all().order_by("-create_time")
        print(db_result)
        # 序列化数据
        order_ser = OrderManyGoodsSerializer(instance=db_result,many=True)
        return ResponseMessage.OrderResponse.success(order_ser.data)

class OrderDetailGenericAPIView(GenericAPIView):
    queryset = Order.objects
    serializer_class = OrderSerializer

    def post(self,request):
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        # email = request.user.get("data").get("username")
        trade_no = request.data.get("trade_no")
        self.get_queryset().filter(trade_no=trade_no).update(**request.data)
        return ResponseMessage.OrderResponse.success("ok")
