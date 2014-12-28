from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)

class Region(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
