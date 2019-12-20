from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def index(request):
    # print(type(request))
    print(request.path)
    return HttpResponse('index')

def login(request):
    # print(request.path)

    # print(request.get_full_path())
    # 获取全部的字段

    # print(request.get_raw_uri())
    # 获取整个网址

    # for key,value in request.META.items():
    #     print("%s:%s"%(key,value))
    #     存储客户端发送来的所有header信息

    # print(request.get_host())
    # 服务器的域名

    print(request.is_ajax())
    # 是否采用ajax
    return HttpResponse('login')