from django.db import models
from django.utils import timezone

class Aquarium(models.Model):
    aq_id = models.IntegerField(primary_key=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    nickname = models.CharField(max_length=50)
    startDate = models.IntegerField()
    
    #def __init__(self, aq_id, size, nickname, startDate, startDateLong):
        #startDateLong = startDate.timestamp()
        
    def __str__(self):
        return self.nickname
    
class Parameter(models.Model):
    param_id = models.IntegerField(primary_key=True)
    p_order = models.IntegerField()
    aq_id = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=50)
    
class Measurement(models.Model):
    measure_id = models.IntegerField(primary_key=True)
    param_id = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.FloatField(null=True,blank=True)
    time = models.BigIntegerField()
    
class PHMeasurement(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    measurement = models.DecimalField(max_digits=3, decimal_places=2)
    measure_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.measurement)

class AquariumImage(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='aquarium_images')
    upload_time = models.DateTimeField(auto_now_add=True)
#    image_path = models.CharField(max_length=1024)

class Reminder(models.Model):
    reminder_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    repeatable = models.BooleanField()
    repeat_time = models.IntegerField()
    start_time = models.DateTimeField()
    notify = models.BooleanField()
    notification_time = models.DateTimeField()
    aquariums = models.ManyToManyField(Aquarium)
    
class Livestock(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE) #TODO keep after deleting a tank? where to put them?
    name = models.CharField(max_length=50)
    
