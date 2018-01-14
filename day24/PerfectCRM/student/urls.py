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
from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.index, name="student_index"),  # 学员首页
    url(r'^my_classes/$', views.my_classes, name="my_classes"),  # 我的班级
    url(r'^my_class_course_record/(?P<class_list_id>\d+)/$',
        views.my_class_course_record, name="my_class_course_record"),  # 我的班级上课记录
]
