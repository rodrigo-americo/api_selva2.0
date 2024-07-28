from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    userName = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    datecreatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.userName

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
