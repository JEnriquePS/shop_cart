# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=11)

    def __str__(self):
        return  "{} - {}".format(self.title, self.cost)

