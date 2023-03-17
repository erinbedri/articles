from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'topic', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.object.slug})


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'topic', 'content')
    success_url = reverse_lazy('articles:article_list')

    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article_list')


