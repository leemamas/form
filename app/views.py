from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django import forms
from django.forms import widgets

class BookForm(forms.Form):
    title = forms.CharField(max_length=32,label='书名')
    price = forms.DecimalField(max_digits=8, decimal_places=2,label='价格')
    date = forms.DateField(
        label = '日期',
        widget=widgets.TextInput(attrs={'type':'date'})
    )
    publish=forms.ModelChoiceField(
        label='出版社',
        queryset=Publish.objects.all(),
        empty_label=None
    )
    authors=forms.ModelMultipleChoiceField(
        label='作者',
        queryset=Author.objects.all()
    )

def book(request):
    list = Book.objects.all()
    return render(request, 'book.html', locals())


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            price = form.cleaned_data.get('price')
            date = form.cleaned_data.get('date')
            publish = form.cleaned_data.get('publish')
            authors = form.cleaned_data.get('authors')

            book = Book.objects.create(title=title, price=price, date=date, publish=publish)
            book.authors.add(*authors)

            return redirect('/book/')

    form = BookForm()

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
