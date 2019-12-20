from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    # a=0
    # b=1
    # c=b/a
    username=request.GET.get('username')
    if not username:
        return redirect(reverse('errors:403'))
    return HttpResponse('首页')