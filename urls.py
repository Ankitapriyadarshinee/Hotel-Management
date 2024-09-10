from django.contrib import admin
from django.urls import path,include
from chat import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('contact',views.contact,name='contact'),
    path('hotels',views.hotels,name='hotels'),
]