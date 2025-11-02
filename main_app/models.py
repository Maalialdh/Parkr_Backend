from django.db import models
from django.contrib.auth.models import User


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

class Car(models.Model):
    model=models.CharField(max_length=50,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.model}"




class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    Parkspot=models.ForeignKey(Parkspot,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.parkingspot}"