from django.db import models

# Create your models here.
class DistInfo(models.Model):
    """省市县地区示例"""
    did = models.IntegerField(primary_key=True, db_column='id')
    dname = models.CharField(max_length=270, db_column='name')
    dparent_id = models.IntegerField(db_column='parent_id')
    dcode = models.CharField(max_length=30, db_column='code')
    dorder = models.IntegerField(db_column='order')

    class Meta:
        managed = False
        db_table = 'district'