from django.db import models
from django.utils import timezone


class PhotoSet(models.Model):
    """A Photoset for the shop"""
    title = models.CharField(max_length=50)
    description = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    price = models.IntegerField(blank=False)
    sales = models.IntegerField(default=0)
    tag = models.CharField(max_length=75, blank=True, null=True)
    preview_image = models.ImageField(upload_to="img")
    photo_set = models.FileField(upload_to=title)

    def __unicode__(self):
        return self.title
