from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    body = models.TextField()
    imag = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def summary(self):
        return(self.body[:100])

    def date_pretty(self):
        return(self.date.strftime("%b %e %Y"))
