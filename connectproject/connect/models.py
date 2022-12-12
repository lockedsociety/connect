from django.db import models
from django.contrib.auth.models import AbstractUser

class Sport(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Human_Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Programming_Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class CLGNIT(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class User(AbstractUser):
    sex = models.CharField(max_length=6)
    age = models.IntegerField()
    sport = models.ManyToManyField(Sport)
    language = models.ManyToManyField(Human_Language)
    programming_language = models.ManyToManyField(Programming_Language)
    profession = models.ManyToManyField(Profession)
    interest = models.ManyToManyField(Interest)
    clgnit = models.ManyToManyField(CLGNIT)
