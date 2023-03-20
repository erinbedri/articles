from django.urls import path, include

from articles import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='article_comment_create'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='article_comment_delete'),
]
