from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Parkinglot (models.Model):
    name =models.CharField(max_length=100)
    location=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"
    

class Parkspot(models.Model):
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
    points=models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.model} -Points: {self.points}"




class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    Parkspot=models.ForeignKey(Parkspot,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    date=models.DateField(auto_now=False, auto_now_add=False)
    is_completed=models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.user.username} - {self.Parkspot} ({'Completed' if self.is_completed else 'Active'})"
    
    