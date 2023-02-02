from __future__ import unicode_literals

from django.db import models

class string(models.Model):
    string = models.CharField(max_length=250)
