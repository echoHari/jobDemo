from django.db import models

# Create your models here.
class jobpost(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name