from django.db import models

class Project(models.Model):
    """docstring for project."""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image=models.ImageField(upload_to='portofolio/images')
    url = models.URLField(blank=True)
