from django.shortcuts import render
from django.template import loader, RequestContext
from  django.http import HttpResponse, JsonResponse
from booktest.models import DistInfo
# Create your views here.

# 自定义的 render 文件
def my_render(request, template_path, context_dict={}):
    # 使用模板文件
    # 1加载模板文件，模板对象
    temp = loader.get_template(template_path)
    # 2、定义模板上下文，给模板文件传递数据
    context = context_dict  # context = RequestContext(request, {})
    # 3、模板渲染：产生标准的html内容
    res_html = temp.render(context)
    # 4、返回给浏览器
    return HttpResponse(res_html)

def index(request):
    book = DistInfo.objects.get(id=1)
    return render(request, 'booktest/index.html',
                  {'book': book})

def index2(request):
    """模板文件的加载数据"""
    return render(request,'booktest/index2.html')

def areas(request):
    """省市县选中案例"""
    return render(request, 'booktest/areas.html',
                  {})
#
# def prov(request):
#     """获取所有省级地区的信息"""
#     areas =