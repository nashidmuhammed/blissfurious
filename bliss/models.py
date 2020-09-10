from django.db import models

# Create your models here.
from django.utils import timezone


class adms(models.Model):
    admin_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class profile(models.Model):
    prof_name = models.CharField(max_length=100)
    prof_img = models.ImageField()
    description = models.TextField()
    cov_img = models.ImageField()
    about = models.TextField()
    email = models.CharField(max_length=100,default='customer.care@blissfurious.com')
    phone = models.CharField(max_length=100,default=9876543210)
    address = models.TextField(default='Kerala')

    def __str__(self):
        return self.prof_name


class article(models.Model):
    art_id = models.AutoField(primary_key=True)
    auther = models.CharField(max_length=100, default='admin')
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    description = models.TextField()
    cover_img = models.ImageField()
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    popular = models.BooleanField(default=False)


class comment(models.Model):
    art_id = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    approval = models.BooleanField(default=False)


class contacts(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,default='Enquiry')
    message = models.CharField(max_length=100)
    replay = models.CharField(max_length=100,default=None,null=True)


class Carousel(models.Model):
    category = models.CharField(max_length=100)
    car_img1 = models.ImageField()
    h_1 = models.CharField(max_length=100, null=True)
    p_1 = models.CharField(max_length=100, null=True)
    car_img2 = models.ImageField()
    h_2 = models.CharField(max_length=100, null=True)
    p_2 = models.CharField(max_length=100, null=True)
    car_img3 = models.ImageField()
    h_3 = models.CharField(max_length=100, null=True)
    p_3 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category