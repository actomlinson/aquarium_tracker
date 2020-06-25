from django.db import models

class Aquarium(models.Model):
    size = models.DecimalField(max_digits=5, decimal_places=2)
    nickname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nickname
    
class PHMeasurement(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    measurement = models.DecimalField(max_digits=3, decimal_places=2)
    measure_time = models.DateTimeField()
    
    def __str__(self):
        return str(self.measurement)

class AquariumImage(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static')
    image_path = models.CharField(max_length=1024)
    
