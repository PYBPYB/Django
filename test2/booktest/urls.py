
from django.urls import path
from booktest import views

app_name = 'booktest'
urlpatterns = [
    path('index/', views.index, name='index'),  # 图书信息页面
    path('create/', views.create, name='create'),  # 新增一本图书
    path('delete/<int:bid>', views.delete, name='delete'),  # 删除点击的图书
]
