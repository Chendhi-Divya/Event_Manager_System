from django.db import models
from django.conf import settings  
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username= None
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True)
    bio = models.TextField(null=True,blank=True )


    hackathon_participant = models.BooleanField(default=True,null=True)




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Event(models.Model):
    Event_title= models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) 
    Event_ID= models.AutoField(primary_key=True)
    Creator_ID=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Date_and_Time=models.DateTimeField()
    Location= models.CharField(max_length=255, null=True, blank=True)
    Calender_link=models.URLField(null=True, blank=True)
    Event_Type=models.CharField(max_length=100, null=True, blank=True)



    
    def __str__(self):
        return self.Event_title
    





class Submission(models.Model):
    participant = models.ForeignKey(User,on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # event_id
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return str(self.event) + '___' + str(self.participant)