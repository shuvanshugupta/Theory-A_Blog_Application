from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('archives',views.archives, name='archives'),
    path('blog',views.blog, name='blog'),
    path('write',views.write, name='write'),
    path('<int:pk>',views.post_detail,name='post_detail'),
    path('<str:category>',views.blog_categorylist,name='blog_categorylist'),
    path('tag'+'/'+'<str:tags>',views.blog_list,name='blog_list'),
]
