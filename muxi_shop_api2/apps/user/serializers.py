import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User
from utils.password_encode import get_md5


class UserSerializer(serializers.ModelSerializer):
    # email作为用户名进行登录，这里我们需要做一个唯一性的验证
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects, message="用户已经存在了")]
    )
    # password = serializers.CharField(write_only=True)
    password = serializers.CharField()
    birthday = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S",required=False)
    # create方法会被自动调用，这里可以做一些数据的验证或者是存储之前数据的加工
    def create(self, validated_data):
        print("create方法被调用了")
        print(validated_data)
        validated_data["password"] = get_md5(validated_data["password"])
        validated_data["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = User.objects.create(**validated_data)
        return result

    class Meta:
        model = User
        fields = "__all__"

