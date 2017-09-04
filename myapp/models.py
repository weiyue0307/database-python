from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=16)

    def __unicode__ (self):
        return self.username

class administrator(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=16)

    def __unicode__ (self):
        return self.username

class dessert_shop(models.Model):
    shopid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    phonenumber = models.CharField(max_length =12,primary_key=True)

    def __unicode__ (self):
        return self.name

class dessert(models.Model):
    dessertid  = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    itshop = models.CharField(max_length=100,null=True)

    def __unicode__ (self):
        return self.name


class comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    content = models.CharField(max_length = 1000)
    dessert_name = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 100)
    dessert_shop_name = models.CharField(max_length = 100)
    comment_date = models.DateField(auto_now_add=True)
    #comment_date.editable = True

    def __unicode__ (self):
        return self.dessert_name


