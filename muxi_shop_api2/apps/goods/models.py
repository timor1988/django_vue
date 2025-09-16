# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import decimal
import json

from django.db import models

from muxi_shop_api2.settings import IMAGE_URL


class Goods(models.Model):
    type_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sku_id = models.CharField(max_length=255, blank=True, null=True)
    target_url = models.CharField(max_length=255, blank=True, null=True)
    jd_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    spu_id = models.CharField(max_length=255, blank=True, null=True)
    mk_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vender_id = models.IntegerField(blank=True, null=True)
    find = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        result = {}
        result['type_id']=self.type_id
        result['name']=self.name
        result['sku_id']=self.sku_id
        result['target_url']=self.target_url
        result['jd_price']=self.jd_price
        result['p_price']=self.p_price
        result['image']= IMAGE_URL + self.image
        result['shop_name']=self.shop_name
        result['shop_id']=self.shop_id
        result['spu_id']=self.spu_id
        result['mk_price']=self.mk_price
        result['vender_id']=self.vender_id
        result['find']=self.find
        return json.dumps(result,cls=DecimalEncoder, ensure_ascii=False)

    class Meta:
        managed = False
        db_table = 'goods'

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,decimal.Decimal):
            return float(o)