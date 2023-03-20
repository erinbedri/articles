from django.contrib import admin

from articles.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'topic', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner', 'article', 'created_at', 'updated_at')


admin.site.register(Comment, CommentAdmin)
