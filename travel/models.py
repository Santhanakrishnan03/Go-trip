from django.db import models

class distination(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.ImageField(upload_to='image')
    offer=models.BooleanField(default=float)
    days=models.IntegerField(default=3)
    location=models.CharField(max_length=100,default='india')
    rate=models.FloatField(max_length=10,default=7)