from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class hirer_profile(models.Model):
    id=models.AutoField
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    company_name=models.TextField(default=0)
    contact=models.IntegerField(default=0)
    email=models.EmailField(default=0)
    userid=models.OneToOneField(User, on_delete=models.CASCADE)
    start_date=models.DateField(default=timezone.now)
    pimage=models.ImageField()
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.userid.username


class post_job(models.Model):
    id = models.AutoField
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    project_name = models.CharField(max_length=50, default="")
    project_description = models.TextField(max_length=250, default="")
    category = models.TextField(max_length=50, default="")
    budget = models.IntegerField(default=0)
    start_time = models.DateField(default=0)
    end_time = models.DateField(default=0)
    ftech = models.TextField(max_length=150, default="")
    btech = models.TextField(max_length=150, default="")
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Title: "+ self.project_name


class job_status(models.Model):
    status_id=models.AutoField
    job_id=models.IntegerField(default=0)
    status=models.IntegerField(default=0)


class payment_hirer(models.Model):
    pid=models.AutoField
    uid=models.OneToOneField(User, on_delete=models.CASCADE)
    job_id=models.IntegerField(default=0)
    payment_amount=models.IntegerField(default=0)

class reviews_hirer(models.Model):
    rhid=models.AutoField
    hid=models.IntegerField(default=0)
    uid=models.OneToOneField(User, on_delete=models.CASCADE)
    hcomments=models.TextField(default=0)