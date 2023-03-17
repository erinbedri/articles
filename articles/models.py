from django.contrib.auth import get_user_model
from django.db import models

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

