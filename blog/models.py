from django.db import models
# Dont forget to make migrations and to migrate!!!
class Blog(models.Model):
    """docstring for Blogs."""
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    URL = models.URLField(blank=True)
    def __str__(self):
        return self.title
