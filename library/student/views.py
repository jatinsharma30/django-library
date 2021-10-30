from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from home.models import BOOK,myUser
# Create your views here.
def index(request):
    books=BOOK.objects.all()
    param={'books':books}
    return render(request,'student/index.html',param)
def wishList(request):
    user=myUser.objects.filter(username="try3@gmail.com")
    return render(request,'student/wishlist.html',{'user':user})
    