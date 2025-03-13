from django.contrib import admin
from blog.models import CategoryModel
from blog.models import ArticleModel

admin.site.register(CategoryModel)
admin.site.register(ArticleModel)

