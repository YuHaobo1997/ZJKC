from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    title = "浙江科创服饰"
    return render(request, 'visitor/homepage.html', {"title": title})
