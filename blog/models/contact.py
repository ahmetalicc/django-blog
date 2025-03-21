from django.db import models


class ContactModel(models.Model):
    email = models.EmailField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"
        verbose_name_plural = "Contacts"
        verbose_name = "Contact"
     

    def __str__(self):
        return self.email