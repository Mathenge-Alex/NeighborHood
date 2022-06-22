from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class NeighborHood(models.Model):
    view =  CloudinaryField("image")
    name = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length = 50,null = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    occupants = models.ForeignKey(User, null = True,related_name='business',on_delete=models.CASCADE)
    
    def save_hood(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def get_all_hoods(cls):
        hood = NeighborHood.objects.all()
        return hood

class Business(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image =  CloudinaryField("image")
    user = models.ForeignKey(User, null = True,related_name='user',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    neighborHood = models.ForeignKey(NeighborHood, null = True,related_name='business',on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']

    def save_business(self):
        self.save()

    def __str__(self):
        return self.name

    @classmethod
    def get_business(cls, profile):
        business = Business.objects.filter(Profile__pk = profile)
        return business
    
    @classmethod
    def get_all_business(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def search(cls,search_term):
        biz = cls.objects.filter(name__icontains=search_term)
        return biz

