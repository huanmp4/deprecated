from django.shortcuts import render
from ..news.models import News

from django.conf import settings
# Create your views here.

def index(request):
    news = News.objects.values().all()

    newss = []

    for index,new in enumerate(news):
        print("=" * 30)
        print("new", new)
        print("index", index)
        new_temp = new
        print("=" * 30)
        # news[index]['content'] = new.content[0:3]
        new_temp["content"] = new["content"][0:10].replace("<p>","").replace("</p>","") + " ```"
        newss.append(new_temp)
    context = {"news":newss}

    return render(request,'flew/index.html',context)


def news_list(request):
    num = 1
    p = int(request.GET.get('p',1))
    print("="*30)
    print('p',p)
    start = p * settings.PAGE_LOAD_NUM
    end = (p+1) * settings.PAGE_LOAD_NUM
    newes = News.objects.order_by('-pub_time')[start:end]
    num += 1
    serializers = NewsSerializers(newes,many=True).data
    content = {'news':serializers}
    return restful.result(data=content)
