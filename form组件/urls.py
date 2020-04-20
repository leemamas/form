
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',book),
    path('book/add/',add_book),
    path('book/edit/<id>/',edit_book),
    path('book/delete/<id>/',delete_book),
]
