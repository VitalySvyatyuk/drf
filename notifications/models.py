from django.db import models


class Office(models.Model):
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class Template(models.Model):
    name = models.CharField(max_length=300)
    sms = models.CharField(max_length=1000)
    email = models.CharField(max_length=2000)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
