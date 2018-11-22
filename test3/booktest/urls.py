from django.urls import path
from booktest import views

app_name = 'booktest'
urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('login_check', views.login_check),  # 登录校验
    path('test_ajax', views.ajax_test),  # 显示ajax
    path('ajax_handle', views.ajax_handle),
    path('login_ajax', views.login_ajax),
    path('login_ajax_check', views.login_ajax_check), #ajax 校验
    path('set_cookie', views.set_cookie),
    path('get_cookie', views.get_cookie),

    path('district', views.district),  # 省市县选中案例
    path('prov', views.prov),  # 获取所有省级地区的信息
    path('city<int:pid>', views.city),  # 获取省下的所有市的信息
    path('dis<int:pid>', views.dis), # 获取省下的所有市的信息
]

