from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django import forms
from django.forms import widgets
from django.forms import ModelForm


class BookModelForm(ModelForm):
    class Meta:
        model=Book
        # fields =['title']
        fields='__all__'
        labels={
            'title':'书名',
            'price':'价格',
            'date':'日期',
            'publish':'出版社',
            'authors':'作者',
        }
        widgets={
            'date':widgets.TextInput(attrs={'type':'date'})
        }

def book(request):
    list = Book.objects.all()
    return render(request, 'book.html', locals())


def add_book(request):
    form = BookModelForm()

    if request.method=='POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/')

    return render(request, 'book_add.html', locals())


def edit_book(request, id):
    book = Book.objects.filter(pk=id).first()
    form = BookModelForm(instance=book)

    if request.method == 'POST':
        form = BookModelForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/book/')

    return render(request, 'book_edit.html', locals())


def delete_book(request, id):
    Book.objects.filter(pk=id).delete()

    return redirect('/book/')
