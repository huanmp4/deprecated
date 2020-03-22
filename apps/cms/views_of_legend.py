from django.shortcuts import render
import json
def legend(request):
    array = json.loads(request.body.decode()).get('array')
    ip = json.loads(request.body.decode()).get('allip')
    servername= json.loads(request.body.decode()).get('servername')

    for i in ip:
        print('ip',i)
    # array = request.POST.get('QueryDict')
    # for a in array:
    #     print('a',a)

    # ip = request.GET.get('ip')
    # machineID = request.GET.get('machineID')



