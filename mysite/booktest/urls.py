from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置
    url('^index$', views.index),  # 建立/index和视图index之间的关系
    url('^index2/*$', views.index2),
    url('^books$', views.show_books),
    url('^books/(\d+)$', views.detail)  # 显示英雄信息
]