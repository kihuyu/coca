# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Datacollection(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    favourite_drink = models.CharField(max_length=50)
    date_of_collection = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='datacollections', on_delete=models.CASCADE)
    def __str__(self):
        return ('%s %s %s %s %s' % (self.name, str(self.latitude), str(self.longitude), self.favourite_drink, str(self.date_of_collection)))


    class Meta:
        ordering = ('date_of_collection',)
