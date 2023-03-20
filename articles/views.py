from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from articles.forms import CommentForm
from articles.models import Article, Comment
from articles.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ArticleListView(OwnerListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')


class ArticleDetailView(OwnerDetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(article=self.object).order_by('-created_at')
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ('title', 'topic', 'content')
    template_name = 'articles/article_create_form.html'

    def get_success_url(self):
        return reverse_lazy('articles:article_detail', kwargs={'slug': self.object.slug})


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ('title', 'topic', 'content')

    def get_success_url(self):
        return reverse_lazy('articles:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(OwnerDeleteView):
    model = Article

    def get_success_url(self):
        return reverse_lazy('articles:article_list')


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        comment = Comment(text=request.POST['comment'], owner=request.user, article=article)
        comment.save()
        return redirect(reverse('articles:article_detail', args=[slug]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment

    def get_success_url(self):
        article = self.object.article
        return reverse('articles:article_detail', args=[article.slug])

