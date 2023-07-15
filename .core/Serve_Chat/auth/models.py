from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db.models.query import QuerySet

class CommunityManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=User.UserType.COMMUNITY)
class IndividualManager(BaseUserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=User.UserType.INDIVIDUAL)

class User(AbstractUser):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    class UserType(models.TextChoices):
        ADMIN="ADMIN","admin"
        COMMUNITY="COMMUNITY","community"
        INDIVIDUAL="INDIVIDUAL","individual"
    base_role=UserType.ADMIN
    role= models.CharField(max_length=50,choices=UserType.choices)
    communities=CommunityManager()
    individual=IndividualManager()
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs) 

class UserProfile(models.Model):
    profile_id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)