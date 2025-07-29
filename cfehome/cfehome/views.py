from django.conf import settings 

from django.shortcuts import render
from django.http import HttpResponse

PROJECT_NAME = getattr(settings,"PROJECT_NAME","Unset Project Name in views")


def hello_world(request):
    return render(request,"hello_world.html",{"project_name":PROJECT_NAME})

def  health_view(request):
    return HttpResponse("ok")