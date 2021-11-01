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


class Theater(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)

    class Meta:
        db_table = 'theater'
        verbose_name = '극장',
        verbose_name_plural = '극장'

    def __str__(self):
        return self.name


class Auditorium(models.Model):
    theater_num = models.ForeignKey(
        Theater, null=True, blank=True, on_delete=models.CASCADE)
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    seats = models.IntegerField()

    class Meta:
        db_table = 'auditorium'
        verbose_name = '상영관',
        verbose_name_plural = '상영관'

    def __str__(self):
        return self.name
