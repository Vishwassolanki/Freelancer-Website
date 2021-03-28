from django.db import models
from django.contrib.auth.models import User
from hirer.models import post_job, hirer_profile
from django.utils import timezone


# Create your models here.

class projects_bids(models.Model):
    objects = None
    id = models.AutoField
    job_id = models.IntegerField(default=0)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    comments = models.TextField(default=0)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.userid
