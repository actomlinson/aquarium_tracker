from django.db import models

class Tank(models.Model):
    size = models.DecimalField(max_digits=5, decimal_places=2)
    nickname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nickname
    
class PHMeasurement(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    measurement = models.DecimalField(max_digits=3, decimal_places=2)
    measure_time = models.DateTimeField()
    
    def __str__(self):
        return str(self.measurement)
