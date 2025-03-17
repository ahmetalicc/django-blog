from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from account.models import CustomUserModel
from ckeditor.fields import RichTextField

class ArticleModel(models.Model):
    image = models.ImageField(upload_to="Article_images")
    title = models.CharField(max_length=50)
    content = RichTextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "title", unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name="Article")
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="Articles")

    class Meta:
        db_table = "article"
        verbose_name_plural = "Articles"
        verbose_name = "Article"
