"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from myblog import views
from myblog import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('classes/', views.classes),

    # api接口
    path('api/', api.api_test),

    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='upload'),  # 固定写法
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),  # 固定写法

]
