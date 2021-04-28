from django.db import models
from django.conf import settings


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=40, default=False, null=True)
    neighborhood = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.neighborhood

class Person(models.Model):
    name        = models.CharField(max_length=100)
    birth_date  = models.DateField()
    email       = models.CharField(max_length=100)
    phone       = models.CharField(max_length=20)
    address     = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    created_data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

