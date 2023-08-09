from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    res = ''
    for c in courses:
        res += f"<br>{str(c)}"

    return HttpResponse(res)
