from django.shortcuts import render
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')


class ArticleDetailView(DetailView):
    model = Article

