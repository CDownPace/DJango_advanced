from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import QueryDict
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    # print(type(request.GET))
    # print(type(request.POST))

    # username=request.GET['username']
    username = request.GET.get('p',default=1)
    # default 表示默认是第一页，如果不传参数会跳到默认
    print(username)
    return HttpResponse('success')

@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method=='GET':
        return render(request,'add_article.html')
    else:
        title=request.POST.get('title')
        content=request.POST.get('content')
        # tags=request.POST.get('tags')
        tags=request.POST.getlist('tags')
        # 有多个相同类名时可以获取出来
        print('title',title)
        print('content',content)
        print('tags',tags)
        return HttpResponse('success')
