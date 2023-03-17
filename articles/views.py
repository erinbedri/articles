from django.urls import reverse_lazy
from articles.models import Article
from articles.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ArticleListView(OwnerListView):
    model = Article
    queryset = Article.objects.all().order_by('-created_at')


class ArticleDetailView(OwnerDetailView):
    model = Article


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

