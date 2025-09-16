# pip install pyjwt
#直接使用django中的key当作盐
import datetime

import jwt

from muxi_shop_api2.settings import SECRET_KEY

# 自定义一个盐
SALT = "SADFSDAFSDFWER"

def create_token():
    headers = {
        'alg':"HS256",
        'typ':"jwt"
    }
    payload = {
        'user_id':1,
        'username':'dazhou',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1) # 定义超时时间
    }

    result = jwt.encode(headers=headers,payload=payload,key=SECRET_KEY,algorithm="HS256")
    return result

def get_payload(token):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
    except jwt.exceptions.DecodeError:
        print("token认证失败了")
    except jwt.exceptions.ExpiredSignatureError:
        print("token已经失效了")
    except jwt.exceptions.InvalidTokenError:
        print("无效的、非法的token")

if __name__ == "__main__":
    # token = create_token()
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRhemhvdSIsImV4cCI6MTY4NDIwODAwMH0.--jZT68z6NLCrwQ9m0IA5zkvBd1yNa1n0vbDjNYbCoI"
    print(token)
    payload = get_payload(token)
    print(payload)