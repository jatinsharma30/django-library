from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_book,name='add_book'),
    # path('signup',views.handleSignup,name='handleSignup'),
    # path('login',views.handleLogin,name='handleLogin'),
    # path('add_book',views.add_book,name="add_book"),
    path('delete_book/<book_id>',views.delete_book,name="delete_book"),
    # path('show',views.show,name='show'),
]
