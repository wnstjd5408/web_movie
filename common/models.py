from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, gender, age, phone_number,  address, password=None):

        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user name')
        if not gender:
            raise ValueError('must have user gender')
        if not age:
            raise ValueError('must have user age')
        if not phone_number:
            raise ValueError('must have user phone_number')
        if not address:
            raise ValueError('must have user address')
        if not password:
            raise ValueError('must have user password')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            phone_number=phone_number,
            address=address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, name, gender, age, phone_number,  address, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            gender=gender,
            age=age,
            phone_number=phone_number,
            address=address,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()
    Gender_choices = {
        ('male', '남'),
        ('female', '여')
    }
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=240, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=Gender_choices)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=240, unique=True)
    address = models.CharField(max_length=250)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'age', 'phone_number', 'address']

    class Meta:
        db_table = 'user'
        verbose_name = '유저',
        verbose_name_plural = '유저'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
