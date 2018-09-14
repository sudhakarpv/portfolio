from django.db import models


class blog(models.Model):
    Title = models.CharField(max_length=50)
    Body = models.CharField(max_length=100)
    Date = models.DateTimeField
    Blog_Image = models.ImageField(upload_to='')
