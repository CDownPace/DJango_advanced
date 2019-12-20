from django.http import HttpResponse,JsonResponse
import json

def index(request):
    response=HttpResponse()
    response.content='学习笔记'
    # content:返回的内容
    response.status_code=400
    # status_code：返回的HTTP响应状态码

    response['X-Token']='admin'
    # 设置请求头
    response.write('admin')
    #  HttpResponse 是一个类似于文件的对象，可以用来写入数据到数据体（content）中。
    return response

def jsonresponse_view(request):
    person={
        'username':'admin',
        'age':18,
        'height':180
    }

    # person_str=json.dumps(person)
    # response=HttpResponse(person_str,content_type='application/json')
    # return response


    # 此处出现错误jsonresponse_view() missing 1 required positional argument: 'request'
    response=JsonResponse(person,safe=False)
    return response