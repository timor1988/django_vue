from rest_framework import serializers

from apps.address.models import UserAddress
from apps.order.models import OrderGoods
from muxi_shop_api2.settings import IMAGE_URL


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"
