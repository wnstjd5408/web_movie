from django.db import models


class Person(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=15)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=240)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)

    class Meta:
        db_table = 'person'
        verbose_name = '유저',
        verbose_name_plural = '유저'
