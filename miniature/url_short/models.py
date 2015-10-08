from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True)
    short_url = models.CharField(max_length=16, blank=True)
    last_updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return self.url

    @staticmethod
    def revert_orig_url(shorturl):
        l = Link.objects.get(short_url=shorturl)
        return l.url
        

