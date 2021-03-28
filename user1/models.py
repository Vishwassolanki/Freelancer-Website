from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class user_profile(models.Model):
    id = models.AutoField
    userid = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    image = models.ImageField
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    Qualification = models.TextField(default="")
    tech_exp = models.TextField(default="")
    exp = models.TextField(default="")
    rate_hr = models.IntegerField(default=0)
    jdate = models.DateField(default=timezone.now)
    status = models.IntegerField(default=0)
    acc_bal = models.IntegerField(default=0)

    def __str__(self):
        return self.fname


class reviews_user(models.Model):
    rhid = models.AutoField
    hid = models.IntegerField(default=0)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    hcomments = models.TextField(default="")


class extendeduser(models.Model):
    id = models.AutoField
    is_admin1 = models.IntegerField(default=0)
    is_user = models.IntegerField(default=0)
    is_hirer = models.IntegerField(default=0)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.User
