from django.db import models

# 设计表

# 图书类(一类)
class BookInfo(models.Model):
    # CharField 指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()

# 英雄人物类（多类）
# 英雄名 hname
# 性别  hgender
# 年龄 hage
# 备注 hcomment

class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)  # False代表男
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 book，建立图书类和英雄类之间的一对多关系
    # 关系属性名对应的表的字段名格式：关系属性名_id
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    # 此参数为了避免两个表里的数据不一致问题，不然会报错：
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)


