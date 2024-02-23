from django.db import models

# Create your models here.

class TextClassification(models.Model):
    text = models.TextField()
    is_hateful = models.BooleanField()

    def __str__(self):
        return self.text