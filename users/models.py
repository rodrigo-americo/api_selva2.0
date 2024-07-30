from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, userName, password=None, **extra_fields):
        if not userName:
            raise ValueError('The User must have a userName')
        user = self.model(userName=userName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userName, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(userName, password, **extra_fields)

class User(AbstractBaseUser):
    userName = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    datecreatedAt = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.userName

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
