from django import http
from django.shortcuts import render, HttpResponse
from web.models import Article

def index(request):
    context = {}
    article_q = Article.objects.all()

    context['articles'] = article_q
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
