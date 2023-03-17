from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'topic', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)

