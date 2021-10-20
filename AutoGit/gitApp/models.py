from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    directory = models.TextField(blank=False)
    branch_name = models.TextField(blank=False)
    default = models.BooleanField(default=False)
    autocommit = models.BooleanField(default=False)
    autocommit_time = models.DateTimeField(default=timezone.now, null=True)
    datetime = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.branch_name)

    class Meta:
        ordering = ['-datetime']


class DefaultProject(models.Model):
    title = models.CharField(max_length=100, blank=False)
    directory = models.TextField(blank=False)
    branch_name = models.TextField(blank=False)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.branch_name)
