from django.shortcuts import render
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

