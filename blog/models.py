from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    body = models.TextField()
    imag = models.ImageField(upload_to='image/')
