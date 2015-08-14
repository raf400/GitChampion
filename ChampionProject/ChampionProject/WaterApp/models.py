from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Staff(models.Model):
    username = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __unicode__(self):
        return self.staff


# creates table for students
class Accounts(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)



    #  Not sure if this is correct, also needs to work with hash
    def __unicode__(self):
        return u' %s %s' % (self.first_name, self.last_name)


# creates table for questions
class Questions(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=2)

    def __unicode__(self):
        return self.question


# Model for a Type, I'm not sure how to link to the Accounts model(or if is correct)
