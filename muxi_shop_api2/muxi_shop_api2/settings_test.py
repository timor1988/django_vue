DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'muxi_shop',
        'USER': 'admin1',
        'PASSWORD': '123',
        'HOST': '192.168.1.129'
    }
}
# 静态文件服务器配置
IMAGE_URL = "http://192.168.1.132:8000/static/product_images/"

# 支付宝沙箱环境配置
APPID="2021000121675750"
# 异步接收rul  post请求
APP_NOTIFY_URL="http://192.168.1.132:8000/pay/alipay/return"
# 同步接收url，就是用户在页面上支付成功之后，然后就跳转的页面  get请求
RETURN_URL="http://192.168.1.132:8000/pay/alipay/return"
# 是否是开发环境
ALIPAY_DEBUG=True

