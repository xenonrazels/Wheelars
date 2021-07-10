from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls  import reverse
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Blog(models.Model):
    objects=models.Manager()
    tag=TaggableManager()
    published=PublishedManager()
    STATUS_CHOICES=[('published','Published'),('draft','Draft')]
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=RichTextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='draft')
    feature_img=models.ImageField(upload_to='blog/{author}/',blank=True)
    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Comment"
        verbose_name_plural="Comments"

