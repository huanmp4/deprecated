



str = "8月/31日/10点30分开放"
str1 = "8月/31日/11点开放"
str2 = "---精品全天固定--1-"
str3 = "8月/31日/★通宵推荐★"

legend = ['11,','22',str2]

import time
import datetime

try:
    spli = legend[2].split("/")
    print("spli原型：",spli)
    print(spli[0])
except:
    if legend[2] == "---精品全天固定---":
        spli = legend[2]
        print("精品全天固定")
        pass
    else:
        # 如果是其它的时间，推进通宵推荐里
        # 获取今天的月和日
        month = time.strftime("%m", time.localtime(time.time()))
        day = time.strftime("%m", time.localtime(time.time()))
        print("month,", month)
        print("day,", day)
        time.strftime("%d", time.localtime(time.time()))
        spli = ["%s月"%month, "%s日"%day, "★通宵推荐★"]
        pass

if spli[-1] == "★通宵推荐★":
    onPage = "allNight"
    ttime = time.strftime('%Y-%m-%d 0:0:0',time.localtime(time.time()))
    dd = ttime
    print("时间1：", dd)

elif spli[0] == "---精品全天固定---":
    onPage = "allDay"
    ttime = time.strftime('%Y-%m-%d 0:0:0',time.localtime(time.time()))
    dd = ttime
    print("时间2：", dd)

else:
    try:
        onPage = "normal"
        year = time.strftime('%Y', time.localtime(time.time()))
        month = spli[0].replace("月", '')
        day = spli[1].replace("日", '')
        hour = spli[2].split("点")[0]
        minute = spli[2].split("点")[1].split("开放")[0].replace('分', '')
        minute = minute if minute != '' else 0
        dd = "%s-%s-%s %s:%s:0" % (year, month, day, hour, minute)
        print("时间3：", dd)
    except:
        month = time.strftime("%m", time.localtime(time.time()))
        day = time.strftime("%m", time.localtime(time.time()))
        time.strftime("%d", time.localtime(time.time()))
        spli = ["%s月" % month, "%s日" % day, "★通宵推荐★"]
