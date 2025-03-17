from django.contrib import admin
from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = (
        "title", "createdAt", "updatedAt"
    )

admin.site.register(ArticleModel, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ("author__username",)
    list_display = ("author", "createdAt" , "updatedAt")

admin.site.register(CommentModel, CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_display = ("email", "createdAt")

admin.site.register(ContactModel, ContactAdmin)

