from django.shortcuts import render
from .models import Article
# from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET,require_POST
from django.http import HttpResponse
# Create your views here.

# @require_http_methods(['GET'])
# 只允许get请求访问

# @require_GET=@require_http_methods(['GET'])
@require_GET
def index(request):
    # 首页会返回所有的文章
    articles=Article.objects.all()
    return render(request,'index.html',context={"articles":articles})
# django.views.decorators.http.require_safe=require_http_methods(['GET','HEAD'])

@require_POST
# 只允许post请求
def add_article(request):
    # 如果使用get请求,就返回html页面.如果使用post请求，就获取提交上来的数据，发送到数据库中
    if request.method=='GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return HttpResponse('success')

