from django.db import models

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    email =  models.CharField(null=False,max_length=255,unique=True,default="10086@qq.com")
    sku_id = models.CharField(null=False,max_length=255,unique=True)
    nums = models.IntegerField()
    is_delete = models.IntegerField()
    class Meta:
        db_table="shopping_cart"