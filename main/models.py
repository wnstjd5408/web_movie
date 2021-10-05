from django.db import models


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    open_movie = models.DateTimeField(null=True)
    director = models.CharField(max_length=300)
    actor = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    runningtime = models.CharField(max_length=50)
    content = models.TextField()
    img = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
