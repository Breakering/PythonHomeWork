"""PerfectCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from PerfectCRM import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django admin
    url(r'^accounts/login/$', views.acc_login),  # 登录
    url(r'^accounts/logout/$', views.acc_logout),  # 注销
    url(r'^crm/', include("crm.urls")),  # crm App
    url(r'^kind_admin/', include("kind_admin.urls")),  # kind_admin 插件
    url(r'^student/', include("student.urls")),  # student app
    url(r'^teacher/', include("teacher.urls")),  # teacher app
]
