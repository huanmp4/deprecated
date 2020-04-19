from django.shortcuts import render

def index(request):
    return render(request,'html_VR/index.html')

def firstPage(request):
    return render(request,'firstPage/index.html')