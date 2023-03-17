from django.urls import path, include

from articles import views

app_name = 'articles'
urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
