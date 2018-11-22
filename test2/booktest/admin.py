from django.contrib import admin
from booktest.models import BookInfo, HeroInfo#, District
# 后台管理相关文件
# Register your models here.
# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    # 改变列表的显示
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'isDelete']
# class DistrictAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'parent_id', 'code' 'order']
# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
# admin.site.register(District, DistrictAdmin)