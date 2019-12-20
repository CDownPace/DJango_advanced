from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv
def index(request):
    response=HttpResponse(content_type='text/csv')
    # with open('xx.csv','w') as fp:
    #     csv.writer(fp)

    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    # attachment 以附件形式下载  filename设置文件名
    writer = csv.writer(response)
    writer.writerow(['username', 'age', 'height', 'weight'])
    # writerow 写入一行
    writer.writerow(['CDownPace', '22', '190', '18'])
    return response


# 写一个模板
def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    context={
        'rows':[
            ['username','age'],
            ['CDownPace',20],

        ]
    }
    template=loader.get_template('abc.txt')
    csv_template=template.render(context)
    return response

class Echo:
    def write(self,value):
        return value
# 大文件
def large_csv_view(request):
    response=StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="large.csv"'
    rows=("Row {},{}\n".format(row,row) for row in range(0,100000))
    # print(type(rows))
    # response.streaming_content=("username,age\n",'CDownPace,98\n')
    response.streaming_content=rows
    # response=HttpResponse('success')
    return response