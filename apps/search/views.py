from django.shortcuts import render,redirect
from apps.news.models import News
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.views import View
from xfz02 import settings
from apps.news.models import News,NewsComment,Category
from django.core.paginator import Paginator
from django.db.models import Q
from urllib import parse

class SearchPagi(View):
    def get(self,request):
        content = request.GET.get('content')
        each_page = request.GET.get('each_page',3) #每页显示3篇
        p_for_web = int(request.GET.get('p_for_web',1)) #获取第几页
        newses = News.objects.select_related('category','author').all()#获取所有数据
        if content:
            newses = newses.filter(Q(title__icontains=content)|Q(content__icontains=content))
        p = Paginator(newses,each_page) #组成每页显示3篇的数据
        page = p.page(p_for_web) #然后显示第几页的数据
        source_urlencode = {
            'content':content or '',
            'each_page':each_page or ''
        }
        urlencode = '&'+parse.urlencode(source_urlencode)

        #每页显示
        source_urlencode2 = source_urlencode
        source_urlencode2.pop('each_page')
        print('source_urlencode', source_urlencode)
        each_page_urlencode = '&'+parse.urlencode(source_urlencode2)

        #title搜索关键字
        source_urlencode3 = source_urlencode
        source_urlencode3.pop('content')
        print('source_urlencode', source_urlencode)
        title_urlencode = '&'+parse.urlencode(source_urlencode3)

        #下面最新两条固定显示
        news_fixed = News.objects.all().select_related('category','author').order_by('pub_time')[:2]

        #===========
        #获取left和right 的页码
        around_count = 2
        current_page = page.number
        num_page = p.num_pages

        left_has_more = False  # 左边还有没有未显示的页码
        right_has_more = False
        # 判断当前页是不是比4小，比如当前页是第二页，他就不能存在 0.1.2.3.4这种情况。
        if current_page <= around_count + 2:
            left_page = range(1, current_page)
        else:
            left_has_more = True
            left_page = range(current_page - around_count, current_page)
        if current_page >= num_page - around_count - 1:
            right_page = range(current_page + 1, num_page + 1)
        else:
            right_has_more = True
            right_page = range(current_page + 1, current_page + 3)
        left_right_page = {
            'left_pages': left_page,
            'right_pages': right_page,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
        }
        #==========

        context = {'page':page,'p':p,'urlencode':urlencode,'each_page_urlencode':each_page_urlencode,'title_urlencode':title_urlencode,'news_fixed':news_fixed}
        context.update(left_right_page)
        return render(request,'search/search.html',context)
    def post(self,request):
        pass


# def search_index(request):
#     # q = request.GET.get('q')
#     # context = {}
#     # if q:
#     #     news = News.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
#     #     context['newses'] = news
#     return render(request, 'search/search.html')
#
#
#
#
# #搜索引擎 全站搜索
# class MySearchHaystack(SearchView):
#     template = 'search.html'
#     #我们通过重写extra_context 来定义我们自己的变量，
#     #通过看源码，extra_context 默认返回的是空，然后再get_context方法里面，把extra_context
#     #返回的内容加到我们self.context字典里
#     def extra_context(self):
#         context = super(MySearchHaystack,self).extra_context()
#         newses = News.objects.select_related('category').order_by('-pub_time').all()[:6]
#         context['newses']= newses
#         return context
#
#     def create_response(self):
#         if not self.request.GET.get('q'):
#             print(self.request.GET.get('q'))
#             search_song = News.objects.select_related('category').order_by('-dynamic_search').all()[:6]
#             Newses = Category.objects.all()
#             paginator = Paginator(Newses, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE)
#             try:
#                 page = paginator.page(int(self.request.GET.get('page',1)))
#             except PageNotAnInteger:
#                 page = paginator.page(1)
#             except EmptyPage:
#                 page = paginator.page(paginator.num_pages)
#             print(page)
#             return render(self.request, self.template, locals())
#         else:
#             qs = super(MySearchHaystack, self).create_response()
#            # print(self.get_context())
#             return qs