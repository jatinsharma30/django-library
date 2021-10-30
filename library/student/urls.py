from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('',views.index,name='index'),
    path('wishList/',views.wishList,name='wishList')
]
