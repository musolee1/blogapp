from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User

# Create your models here.

#blogs/1.jpeg
#movies/5.jpeg

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    image = models.ImageField(default="fallback.webp", blank=True, upload_to="blogs")
    description = models.TextField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable = False)
    categories = models.ManyToManyField(Category, blank = True)
    blog_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title}"
    
    def _str_(self):
        return f"{self.blog_date}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_date.strftime("%d %B %Y %H:%M")