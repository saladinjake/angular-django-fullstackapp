from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    #pass
    model = Book
    template_name = "allbooks.html"
