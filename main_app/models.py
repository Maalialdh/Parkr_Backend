from django.db import models

# Create your models here.
class Parkinglot (models.Model):
    name =models.CharField(max_length=100)
    location=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"
    

class Parkspot(models.Model):
    # spot_number=models.CharField(max_length=10)
    status = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('reserved', 'Reserved'), ('occupied', 'Occupied')],
        default='available')
    parkinglot=models.ForeignKey(Parkinglot,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} - {self.parkinglot.name}"
    
class Reservation(models.Model):
    pass