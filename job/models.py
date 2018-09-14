from django.db import models


class job (models.Model):
    Image = models.ImageField(upload_to='')
    Char = models.CharField(max_length=200)
