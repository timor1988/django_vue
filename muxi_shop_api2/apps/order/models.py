# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Order(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    trade_no = models.CharField(max_length=155, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    pay_status = models.CharField(max_length=155, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    ali_trade_no = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    # update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderGoods(models.Model):
    trade_no = models.CharField(max_length=255, blank=True, null=True)
    sku_id = models.CharField(max_length=255, blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)
    # create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_goods'
