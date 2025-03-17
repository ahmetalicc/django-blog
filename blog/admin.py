from django.contrib import admin
from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

admin.site.register(CategoryModel)

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = (
        "title", "createdAt", "updatedAt"
    )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("author__username",)
    list_display = ("author", "createdAt" , "updatedAt")

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "createdAt")


