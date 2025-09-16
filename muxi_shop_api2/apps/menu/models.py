import json

from django.db import models

# Create your models here.

class MainMenu(models.Model):
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    # 在这里我们自己手动序列化
    def __str__(self):
        result = {}
        result['main_menu_id'] = self.main_menu_id
        result["main_menu_name"] = self.main_menu_name
        # result["main_menu_url"] = self.main_menu_url
        return json.dumps(result,ensure_ascii=False)


    class Meta:
        managed = False
        db_table = 'main_menu'


class SubMenu(models.Model):
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        result = {}
        result["main_menu_id"]=self.main_menu_id
        result["sub_menu_id"]=self.sub_menu_id
        result["sub_menu_type"]=self.sub_menu_type
        result["sub_menu_name"]=self.sub_menu_name
        return json.dumps(result,ensure_ascii=False)

    class Meta:
        managed = False
        db_table = 'sub_menu'
