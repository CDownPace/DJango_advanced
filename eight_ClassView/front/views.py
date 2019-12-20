from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Article
from django.views.generic import ListView,View
from django.utils.decorators import method_decorator

# Create your views here.

def add_article(request):
    articles=[]
    for x in range(0,102):
        article=Article(title='标题:%s'%x,content='内容:%s'%x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('article added successfully')


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list1.html'
    paginate_by =10
    context_object_name = 'articles'
    ordering = 'create_time'
    page_kwarg = 'p'
    # 首先 ArticleListView 是继承自 ListView 。
    # 2. model ：重写 model 类属性，指定这个列表是给哪个模型的。
    # 3. template_name ：指定这个列表的模板。
    # 4. paginate_by ：指定这个列表一页中展示多少条数据。
    # 5. context_object_name ：指定这个列表模型在模板中的参数名称。
    # 6. ordering ：指定这个列表的排序方式。
    # 7. page_kwarg ：获取第几页的数据的参数名称。默认是 page 。

    def get_context_data(self, **kwargs):
        context=super(ArticleListView,self).get_context_data(*kwargs)
        context['username']='CDownPace'
        # print('='*30)
        # print(context)
        # print('='*30)

        paginator=context.get('paginator')
        page_obj=context.get('page_obj')
        pagenation_data=self.get_pagination_data(paginator,page_obj)
        context.update(pagenation_data)
        # print(paginator.count)
        # Paginator常用属性和方法:count ：总共有多少条数据

        # print(paginator.num_pages)
        # Paginator常用属性和方法:num_pages：总共有多少页

        # print(paginator.page_range)
        # Paginator常用属性和方法:page_range ：页面的区间。比如有三页，那么就 range(1,4)

        # page_obj=context.get('page_obj')
        # print(page_obj.has_next())
        # Page常用属性和方法：has_next ：是否还有下一页。
        # 2. has_previous ：是否还有上一页。
        # 3. next_page_number ：下一页的页码。
        # 4. previous_page_number ：上一页的页码。
        # 5. number ：当前页。
        # 6. start_index ：当前这一页的第一条数据的索引值。
        # 7. end_index ：当前这一页的最后一条数据的索引值。


        return context
    # 8. get_context_data ：获取上下文的数据。


    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=9)
    # 9. get_queryset ：如果你提取数据的时候，并不是要把所有数据都返回，
    # 那么你可以重写这个 方法。将一些不需要展示的数据给过滤掉。
    # 获取id小于9的


    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page=page_obj.number
        num_pages=paginator.num_pages

        left_has_more=False
        right_has_more=False

        if current_page<=around_count+2:
            left_pages=range(1,current_page)
        else:
            left_has_more=True
            left_pages=range(current_page-around_count,current_page)

        if current_page>=num_pages-around_count-1:
            right_pages=range(current_page+1,num_pages+1)
        else:
            right_has_more=True
            right_pages=range(current_page+1,current_page+around_count+1)



        return{
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'num_pages':num_pages
        }

def login_required(func):
    def wrapper(request,*args,**kwargs):
        username=request.GET.get('username')
        if username:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('front:login'))
    return wrapper


@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        return HttpResponse("个人中心界面")

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView,self).dispatch(request,*args,**kwargs)

def login(request):
        return HttpResponse('login')