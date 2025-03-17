from django.db import models
from blog.models import ArticleModel
from account.models import CustomUserModel
from blog.models.abstract_models import DateAbstractModel


class CommentModel(DateAbstractModel):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="comment")
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
  
    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.author.username