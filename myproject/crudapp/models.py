from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, null=True, blank=True)  # New field for country

    def __str__(self):
        return self.name
