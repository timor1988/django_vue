import datetime

import jwt
from rest_framework.authentication import BaseAuthentication

from muxi_shop_api2.settings import SECRET_KEY

def create_token(payload,timeout=100000):
    headers = {
        'alg':"HS256",
        'typ':"jwt"
    }
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)

    result = jwt.encode(headers=headers,payload=payload,key=SECRET_KEY,algorithm="HS256")
    return result

def get_payload(token):
    result = {"status":False,"data":None,"error":None}
    try:
         payload = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
         result["status"] = True
         result["data"] = payload
    except jwt.exceptions.DecodeError:
        print("token认证失败了")
        result["error"] = "token认证失败了"
    except jwt.exceptions.ExpiredSignatureError:
        print("token已经失效了")
        result["error"] = "token已经失效了"
    except jwt.exceptions.InvalidTokenError:
        print("无效的、非法的token")
        result["error"] = "无效的、非法的token"
    return result

# 用户在url中进行token的参数配置
class JwtQueryParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 从url中拿到token
        token = request.GET.get("token")
        result_payload = get_payload(token)
        print(result_payload)
        return (result_payload,token)

class JwtHeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 从头信息中拿到token
        # print(request.META)
        # token = request.META.get("HTTP_TOKEN")  postman中这样获取
        token = request.META.get("HTTP_AUTHORIZATION")  # 谷歌浏览器中这样获取
        print(token)
        result_payload = get_payload(token)
        print(result_payload)
        return (result_payload,token)
