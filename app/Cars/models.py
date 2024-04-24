from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    currentdate = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    

    def __str__(self):
        return self.name
    
    
    
    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
    
 
    