from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
# Create your views here.
from .models import allIP,Array,WebSite,WebSiteClick
from django.db.models import F
from utils import restful


#远程访问收集数据
def index(request):
    array = json.loads(request.body.decode()).get('array')
    allip = json.loads(request.body.decode()).get('allip')
    servername = json.loads(request.body.decode()).get('servername')
    for a in array:
        username = a["username"]
        gold = a["元宝"]
        machine = a["机器码"]
        servername = servername
        character = a['character']
        ip = a["ip"]
        if username != ''and username != None:
            try:
                exist = Array.objects.get(username=username)
                if exist:
                    exist.gold = F('gold') + gold
                    exist.save()
                else:
                    print('传奇查不到该用户名')
            except:
                #是否在网站登录过的
                exist = WebSite.objects.filter(ip=ip).exists()
                if exist:
                    websites = WebSite.objects.get(ip=ip)
                    array = Array.objects.create(username=username, gold=gold, machine=machine, servername=servername,character=character,ip=ip,website=websites)
                    array.save()
                else:
                    array = Array.objects.create(username=username, gold=gold, machine=machine, servername=servername,character=character, ip=ip)
                    array.save()
        else:
            print('用户名不存在，不再继续增加')
    for ip in allip:
        try:
            exit = allIP.objects.filter(ip = ip).exists()
            if not exit:
                web_exist = WebSite.objects.filter(ip=ip).exists()
                if web_exist:
                    web = WebSite.objects.get(ip=ip)
                    print('web',web)
                    print('web.advertisement_id',web.advertisement_id)
                    save_IP = allIP.objects.create(ip=ip,advertisement=web,websitename=web.advertisement)

                    save_IP.save()
                else:
                    save_IP = allIP.objects.create(ip=ip)
                    save_IP.save()
            else:
                print('200,ip已存在')
        except:
            print('这里出错:exit = allIP.objects.filter(ip = i).exists()')

#获取当前IP当转接
def visit(request):
    name = request.GET.get('name')
    http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    try:
        click = WebSiteClick.objects.get(name=name)
        print('%s已访问'%name)
        click.click = F("click")+1
        click.save()
    except:
        pass
    if http_x_forwarded_for:
        ip_addr = http_x_forwarded_for.split(',')[0]
        #斯洛文尼亚
        invalid_save_address_by_138ip(ip = ip_addr,name =name)

        #当前IP
    else:
        ip_addr2 = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        #法西兰
        invalid_save_address_by_138ip(ip=ip_addr2, name=name)


    return HttpResponseRedirect('http://cg.yy1ng.com/')

def invalid_save_address_by_138ip(ip,name):
    ip = ip or '无'
    print('ip:',ip)
    try:
        exist = WebSite.objects.filter(ip=ip).exists()
        if exist:
            pass
        else:
            click = WebSiteClick.objects.get(name=name)
            address = WebSite.objects.create(ip=ip, advertisement=click,)
            address.save()
    except:
        pass

def check(request):
    array = Array.objects.all()
    allip = allIP.objects.all()
    website = WebSite.objects.all()
    click =  WebSiteClick.objects.all()
    tomjjj = WebSiteClick.objects.get(id=1).website_set.all()
    tom2hq = WebSiteClick.objects.get(id=2).website_set.all()
    cq9pkenter = WebSiteClick.objects.get(id=3).website_set.all()
    tom6xq = WebSiteClick.objects.get(id=4).website_set.all()

    # 反查WEb jjj有多少人充值
    #获取进入网站并充值的用户
    jjjenter = tomjjj.count()
    cq6xqenter = tom6xq.count()
    cq9pkenter = cq9pkenter.count()
    cq2hbenter = tom2hq.count()

    clickCount = 0
    for c in click:
        clickCount += c.click


    allipCount = allip.count()
    arrayCount = array.count()
    websiteCount = website.count()
    content = {
        "array":array,
        "allip":allip.count(),
        "website":website,
        "allipCount":allipCount,
        "arrayCount":arrayCount,
        "websiteCount":websiteCount,
        "click":click,
        "clickCount":clickCount,
        "jjjenter":jjjenter,
        "cq9pkenter":cq9pkenter,
        "cq2hbenter":cq2hbenter,
        "cq6xqenter":cq6xqenter,

    }
    return render(request,'legendCMS/check.html',content)