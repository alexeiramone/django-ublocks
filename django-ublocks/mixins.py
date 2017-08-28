# -*- coding: utf-8 -*-
from django.db import models

class AutomaticDatesMixin(models.Model):
    date_created = models.DateTimeField('Date Created', auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField('Date Last Updated', auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True

