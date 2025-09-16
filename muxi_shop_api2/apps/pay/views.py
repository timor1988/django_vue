from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from datetime import datetime

from apps.order.models import Order
from apps.pay.alipay import AliPay


# Create your views here.
class ToAliPayPageAPIView(APIView):
    def post(self, request):
        # trade_no = "123"
        # subject="我是主题"
        # total_amount="1"
        if not request.user.get("status"):
            return JsonResponse(request.user,safe=False)
        trade_no = request.data.get("tradeNo")
        total_amount = request.data.get("orderAmount")
        alipay = AliPay()
        url = alipay.direct_pay(
            out_trade_no=trade_no,
            subject = "主题:"+trade_no,
            total_amount = total_amount,
        )
        # print(url)
        re_url = alipay.gateway + "?{data}".format(data=url)
        print(re_url)
        return JsonResponse({"alipay":re_url})

class AlipayAPIView(APIView):
    def get(self, request):
        processed_dict = {}
        for k,v in request.GET.items():
            processed_dict[k] = v
        sign = processed_dict.pop("sign",None)
        alipay = AliPay()
        is_verify = alipay.verify(processed_dict, sign)
        if is_verify is True:
            trade_no = processed_dict.get('out_trade_no')
            ali_trade_no = processed_dict.get('trade_no')
            # 0待支付  1 待确认  2支付完成  3 已完成
            pay_status = 2
            Order.objects.filter(trade_no=trade_no).update(
                ali_trade_no=ali_trade_no,
                pay_status=pay_status,
                pay_time=datetime.now()
            )
        return redirect("http://127.0.0.1:8080/profile?activeIndex=3")

    def post(self,request):
        processed_dict = {}
        for k, v in request.POST.items():
            processed_dict[k] = v
        sign = processed_dict.pop("sign", None)
        alipay = AliPay()
        is_verify = alipay.verify(processed_dict, sign)
        if is_verify is True:
            trade_no = processed_dict.get('out_trade_no')
            ali_trade_no = processed_dict.get('trade_no')
            # 0待支付  1 待确认  2支付完成  3 已完成
            pay_status = 2
            Order.objects.filter(trade_no=trade_no).update(
                ali_trade_no=ali_trade_no,
                pay_status=pay_status,
                pay_time=datetime.now()
            )
        return redirect("http://127.0.0.1:8080/profile?activeIndex=3")