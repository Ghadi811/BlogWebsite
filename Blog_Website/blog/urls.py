from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.myusers, name='users'),
    path('blogs/', views.mypost, name='blog'),
    path('blogs/blogdetails/<int:id>/', views.blogdetails, name='blogdetails'),
    path('blogs/blogdetails/comments/<int:id>/', views.mycomment, name='comments'),
    path('categories/', views.mycategory, name='categories'),
    path('admin/', admin.site.urls),
]
