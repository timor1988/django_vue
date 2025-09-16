import json
from base64 import encodebytes, decodebytes
from datetime import datetime
from urllib.parse import quote_plus

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from django.conf import settings
from Crypto.PublicKey import RSA

class AliPay():
    def __init__(self):
        self.appid = settings.APPID
        self.app_notify_url=settings.APP_NOTIFY_URL
        self.return_url=settings.RETURN_URL
        self.debug=settings.ALIPAY_DEBUG
        self.app_notify_url=settings.APP_NOTIFY_URL
        self.app_private_key_path=settings.PRIVATE_KEY_PATH
        self.ali_pub_key_path=settings.ALI_PUB_KEY_PATH
        self.app_private_key = None
        self.ali_pub_key = None

        with open(self.app_private_key_path) as fp:
            self.app_private_key = RSA.importKey(fp.read())

        with open(self.ali_pub_key_path) as fp:
            self.ali_pub_key = RSA.importKey(fp.read())

        if self.debug is True:
            self.gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.gateway = "https://openapi.alipay.com/gateway.do"

    # 解析必要参数
    def direct_pay(self, subject, out_trade_no, total_amount, **kwargs):
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY",
        }

        biz_content.update(kwargs)
        data = self.build_body("alipay.trade.page.pay", biz_content, self.return_url)
        return self.sign_data(data)

    #  构建公共请求参数
    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,
            "method": method,
            "charset": "utf-8",
            "sign_type": "RSA2",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "biz_content": biz_content
        }

        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url

        return data

    # 数据签名逻辑
    def sign_data(self, data):
        # 如果有，清除掉这个不必要的参数，后边自己加
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = self.order_data(data)
        unsigned_string = "&".join("{0}={1}".format(k, v) for k, v in unsigned_items)
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string.encode("utf-8")))
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        quoted_string = "&".join("{0}={1}".format(k, quote_plus(v)) for k, v in unsigned_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    def order_data(self, data):
        complex_keys = []
        for key, value in data.items():
            if isinstance(value, dict):
                complex_keys.append(key)

        # 将字典类型的数据dump出来
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))

        return sorted([(k, v) for k, v in data.items()])


    def _verify(self, raw_content, signature):
        # 开始计算签名
        key = self.ali_pub_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False

    # 签名验证逻辑
    def verify(self, data, signature):
        if "sign_type" in data:
            sign_type = data.pop("sign_type")
        # 排序后的字符串
        unsigned_items = self.order_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)
