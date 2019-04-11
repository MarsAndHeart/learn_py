"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.http import HttpResponse
from django.conf.urls import url
import json

from . import view


# 接收GET请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


# 接收POST请求数据
def search_post(request):
    print(request)
    reqJson = json.loads(request.body)
    ctx = {
        'status': '0000',
        'q': reqJson['q']
    }
    # if request.POST:
    #     print('hello--------')
    #     ctx['rlt'] = request.POST['q']
    print(ctx)
    return HttpResponse(json.dumps(ctx))


urlpatterns = [
    url(r'^$', view.home),
    url(r'^hello$', view.hello),
    url(r'^search$', search),
    url(r'^search_post$', search_post),
    url('', view.notFound),
]
