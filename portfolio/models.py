from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title + ' - ' + str(self.author)