from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """docstring for project."""

    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True,max_length=5000)
    #image=models.ImageField(upload_to='portofolio/images')
    #url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True,blank=True)
    #completion = models.BooleanField(default=False,name='Completion Status')
    importance = models.BooleanField(default=False,name='Important')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
