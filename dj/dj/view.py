from django.http import HttpResponse


def home(request):
    return HttpResponse('this is home page')


def hello(request):
    return HttpResponse('hello world')


def notFound(request):
    return HttpResponse('404 not found')
