from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    directory = models.TextField(blank=False)
    branch_name = models.TextField(blank=False)
    default = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.branch_name)
