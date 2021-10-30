from django.shortcuts import render,redirect
from home.models import BOOK
from django.contrib import messages 

# Create your views here.

#add book
def add_book(request):
    if request.method=='POST':
        name=request.POST['bookName']
        author=request.POST['author']
        genre=request.POST['genre']
        if len(name)>2 and len(author)>2 and genre!="":
            book=BOOK(name=name,author=author,genre=genre)
            book.save()
            messages.success(request, "book has been successfully added")
        else:
            messages.error(request, "Please fill the form correctly")
    books=BOOK.objects.all()
    param={'books':books}
    return render(request,'teacher/index.html',param)

#delete a book
def delete_book(request,book_id):
    book=BOOK.objects.get(pk=book_id)
    print(book)
    book.delete()
    messages.success(request,"Book has been deleted successfully")
    return redirect('add_book')