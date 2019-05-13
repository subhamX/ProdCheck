from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    address = models.CharField(max_length=100)
    admin = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    
    # image = models.ImageField()
    # Here ForeignKey isn't working! Check Out
    # admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    avail = models.BooleanField(default= False)
    shopProfile = models.ForeignKey(Shop, on_delete=models.CASCADE)
    desc = models.TextField()
    # image = models.ImageField()
    def __str__(self):
        return self.name
