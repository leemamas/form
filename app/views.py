from django.shortcuts import render, redirect, HttpResponse
from .models import *

def book(request):
    list = Book.objects.all()
    return render(request, 'book.html', locals())

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        authors = request.POST.getlist('authors')

        book_obj = Book.objects.create(title=title, price=price, date=date, publish_id=publish)
        book_obj.authors.add(*authors)

        return redirect('/book/')

    publishs = Publish.objects.all()
    authors = Author.objects.all()
    return render(request, 'book_add.html', locals())


def edit_book(request, id):
    book = Book.objects.filter(pk=id).first()
    publishs = Publish.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        authors = request.POST.getlist('authors')

        Book.objects.filter(pk=id).update(title=title, price=price, date=date, publish_id=publish)
        book.authors.set(authors)

        return redirect('/book/')

    return render(request, 'book_edit.html', locals())


def delete_book(request, id):
    Book.objects.filter(pk=id).delete()

    return redirect('/book/')
