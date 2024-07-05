from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    post_tags = models.CharField(max_length=255, default="Technology", verbose_name='Tags')
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    feature_image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_id = models.CharField(max_length=3, unique=True, default=1)

    def __str__(self):
        return self.category_name

class QuesModel(models.Model):
    question = models.CharField(max_length=900,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.question

