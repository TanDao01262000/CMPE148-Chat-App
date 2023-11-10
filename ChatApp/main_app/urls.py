from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   # path('', views.index, name="index"),
    path('', views.frontpage, name='frontpage'),
    path('login/', views.loginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
   # path('home/', views.home, name='home'),
    path("<str:room_name>/", views.room, name="room"),
    
]