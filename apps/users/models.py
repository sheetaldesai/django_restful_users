# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated', null = True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    