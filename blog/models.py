from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish'
                            )
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices= Status,
        default=Status.DRAFT
    )
    photo = models.ImageField(
        upload_to = 'user/%Y/%m/%d',
        blank=True
    )
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
class Portfolio(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        upload_to='user/%Y/%m/%d',
        blank=True
    )

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]

    def __str__(self):
        return self.name


































