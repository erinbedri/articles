from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Article(models.Model):
    ARTICLE_TOPICS = (
        ('Romantic Relationships', 'Romantic Relationships'),
        ('Family/Friends', 'Family/Friends'),
        ('Recreation/Hobbies', 'Recreation/Hobbies'),
        ('Work', 'Work'),
        ('Identity/Appearance', 'Identity/Appearance'),
        ('Food', 'Food'),
        ('Environmental Issues', 'Environmental Issues'),
        ('Technology', 'Technology'),
        ('History', 'History'),
        ('Politics/Government', 'Politics/Government'),
        ('Sports', 'Sports'),
        ('Health', 'Health'),
        ('Transportation', 'Transportation'),
        ('Arts/Entertainment/Media', 'Arts/Entertainment/Media'),
        ('Values', 'Values'),
    )

    ARTICLE_TOPICS_MAX_LENGTH = max([len(topic[0]) for topic in ARTICLE_TOPICS])

    title = models.CharField(max_length=150)
    topic = models.CharField(max_length=ARTICLE_TOPICS_MAX_LENGTH, choices=ARTICLE_TOPICS)
    content = models.TextField(max_length=2500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

