from django.contrib import admin
from blog.models import CategoryModel, ArticleModel

admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = (
        "title", "createdAt", "updatedAt"
    )

admin.site.register(ArticleModel, ArticleAdmin)

