from django.contrib import admin
from booktest.models import District
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'order']

# 注册模型类
admin.site.register(District, DistrictAdmin)