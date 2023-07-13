from django.shortcuts import render

from app.forms import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WPMO=WebpageModelForm()
    d={'WPMO':WPMO}

    if request.method=='POST':
        WPMFD=WebpageModelForm(request.POST)
        if WPMFD.is_valid():
            WPMFD.save()
        return HttpResponse('webpage data inserted')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}

    if request.method=='POST':
        ARMFOD=AccessRecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse("Insertion of data is done successfully")

    return render(request,'insert_accessrecord.html',d)