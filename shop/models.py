from django.db import models
from django.utils import timezone


class PhotoSet(models.Model):
    """A Photoset for the shop"""
    title = models.CharField(max_length=50)
    description = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    price = models.DecimalField(blank=False, default=10, decimal_places=2, max_digits=5)
    sales = models.IntegerField(default=0)
    preview_image = models.ImageField(upload_to="img")
    photo_set = models.FileField(upload_to="photosets")

    def __unicode__(self):
        return self.title
