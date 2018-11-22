from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from booktest.models import District
# Create your views here.
def index(request):
    book = District.objects.get(id=1)
    return render(request, 'booktest/index.html',
                  {'book': book})

def login(request):
    """显示登陆界面"""
    # 获取cookie
    if 'username'and'password' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
        password = request.COOKIES['password']
    else:
        username = ''
        password = ''

    return render(request, 'booktest/login.html',
                  {'username': username,
                   'password': password})

def login_check(request):
    """登录校验视图"""
    # request.POST 保存的是 post方式 提交的参数 QueryDict
    # request.GET 保存的是 get方式 提交的参数 QueryDict
    # 1、获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 2、进行登陆的校验
    # 世纪开发中，用户名和密码应该在数据库里
    if username == '123' and password == '123':
        # 正确，到首页
        response = redirect('/index')
        # 判断是否需要记住用户名
        if remember == 'on':
            response.set_cookie('username', username)
            response.set_cookie('password', password)
        return response
    else:
        # 错误，跳转到登录界面
        return redirect('/login')
    # 3、返回应答

def ajax_test(request):
    """显示ajax页面"""
    return render(request, 'booktest/test_ajax.html')

def ajax_handle(request):
    """ajax请求处理"""
    # 返回的json数据 {'res':1}
    return JsonResponse({'res': 1})

def login_ajax(request):
    """显示ajax登陆界面"""
    return render(request, 'booktest/login_ajax.html',
                  {})

@csrf_exempt
def login_ajax_check(request):
    """ajax登录校验"""
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == '123' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

# /set_cookie
def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse('设置cookie')
    response.set_cookie('num', 1,)
    return response

def get_cookie(request):
    """获取cookie的信息"""
    return HttpResponse(request.COOKIES['num'])

def district(request):
    """省市县选中案例"""
    return render(request, 'booktest/district.html',
                  {})

def prov(request):
    """获取所有省级地区的信息"""
    areas = District.objects.filter(parent_id=0)
    areas_list = []
    # 遍历areas 拼接出json数据:id,name，parent_id
    for area in areas:
        areas_list.append((area.id, area.name))
    return JsonResponse({'data': areas_list})

def city(request, pid):
    """获取该省下所有市的信息"""
    areas = District.objects.filter(parent_id=pid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.name))
    return JsonResponse({'data': areas_list})

def dis(request, pid):
    """获取该省下所有市的信息"""
    areas = District.objects.filter(parent_id=pid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.name))
    return JsonResponse({'data': areas_list})
