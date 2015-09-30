from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()

    @staticmethod
    def shorten(longurl):
        return "h"

