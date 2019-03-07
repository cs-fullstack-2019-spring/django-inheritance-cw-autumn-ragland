from django.db import models


# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.name
