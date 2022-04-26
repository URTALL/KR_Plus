from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения - менеджеры")

def about(request, catid):
    return HttpResponse(f"О компании в каталоге <br> {catid}")




def PageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")