from rest_framework import serializers
from .models import Parkinglot,Parkspot


class ParkinglotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkinglot
        fields = '__all__'



class ParkspotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parkspot
        fields = '__all__'

