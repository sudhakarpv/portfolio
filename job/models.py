from django.db import models


class job (models.Model):
    Image = models.ImageField(upload_to='images/')
    Char = models.CharField(max_length=200)
