from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticleModel


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.author.username