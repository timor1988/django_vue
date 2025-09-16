from rest_framework import serializers

from apps.cart.models import Cart
from apps.goods.models import Goods
from apps.goods.serializers import GoodsSerializer


class CartSerializer(serializers.ModelSerializer):
    sku_id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    class Meta:
        model = Cart
        fields = "__all__"

class CartDetailSerializer(serializers.Serializer):
    sku_id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    nums = serializers.IntegerField()
    is_delete = serializers.IntegerField()
    # 关键的是我接下来要写的内容
    goods = serializers.SerializerMethodField()

    def get_goods(self,obj):
        # print(obj)
        # ser = GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).all(),many=True).data
        ser = GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).first()).data
        return ser
