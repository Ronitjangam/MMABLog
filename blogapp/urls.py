from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.home),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='login'),
    path('register',views.register_view,name='register'),
    path('add-blog',views.add_blog,name='add_blog'),
    path('blog_detail/<slug>',views.blog_detail,name='blog_detail'),
]
