from django.db import models
from django.conf import settings

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Mail = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Description = models.TextField()

    def __str__(self):
        return self.name
