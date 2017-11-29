# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list

class Cart(models.Model):
    user = models.ForeignKey(User)
    item = models.CharField(max_length=10000, validators=[validate_comma_separated_integer_list])
    cost = models.DecimalField(decimal_places=2, max_digits=11)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.user, self.cost)

