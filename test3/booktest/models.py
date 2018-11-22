from django.db import models

# Create your models here.
class District(models.Model):

    id = models.IntegerField(primary_key=True, null=False, default=False)
    name = models.CharField(max_length=270, null=True, default=False)
    parent_id = models.IntegerField(null=True, default=False)
    code = models.CharField(max_length=30, null=True, default=False)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'district'
