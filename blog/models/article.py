from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from account.models import CustomUserModel
from ckeditor.fields import RichTextField
from blog.models.abstract_models import DateAbstractModel

class ArticleModel(DateAbstractModel):
    image = models.ImageField(upload_to="Article_images")
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from = "title", unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name="Article")
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="Articles")

    class Meta:
        db_table = "article"
        verbose_name_plural = "Articles"
        verbose_name = "Article"
