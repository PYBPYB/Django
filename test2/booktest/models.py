from django.db import models

class BookInfoManager(models.Manager):
    """图书模型管理器类"""
    # 1、改变查询的结果集
    # 2、封装函数，操作模型类对应的数据表
    pass

# 图书类(一类)
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    # object = BookInfoManager()  # 自定义一个BookInfoManager对象

    # class Meta:
        # db_table = 'bookinfo'   # 指定模型类对应的表名


class HeroInfo(models.Model):
    """英雄人物模型类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)  # False代表男
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 book，建立图书类和英雄类之间的一对多关系
    # 关系属性名对应的表的字段名格式：关系属性名_id
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题，不然会报错：
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # 删除标记
    isDelete = models.BooleanField(default=False)

# class District(models.Model):
#
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=270, blank=True)
#     parent_id = models.IntegerField(blank=True)
#     code = models.CharField(max_length=30, blank=True)
#     order = models.IntegerField(blank=True)
#
#     class Meta:
#         managed = False
#         db_table = 'district'

