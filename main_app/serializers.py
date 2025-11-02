from rest_framework import serializers
from .models import Parkinglot,Parkspot,Car,Reservation
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ParkinglotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkinglot
        fields = '__all__'



class ParkspotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkspot
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
