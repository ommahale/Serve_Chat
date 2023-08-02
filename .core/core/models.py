from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid4,primary_key=True)

class CommunityPage(BaseModel):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

class SubGroups(BaseModel):
    community = models.ForeignKey(CommunityPage,on_delete=models.CASCADE)

class MemberProfile(BaseModel):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    community = models.ForeignKey(CommunityPage, on_delete=models.CASCADE)
    subGroups = models.ManyToManyField(SubGroups,blank=True)
