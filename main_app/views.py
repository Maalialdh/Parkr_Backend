from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Parkinglot,Parkspot
from .serializers import ParkinglotSerializer, ParkspotSerializer


# Create your views here.
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the api home route!'}
        return Response(content)



class Parkinglot(APIView):
    queryset=Parkinglot.objects.all()
    serializer_class=ParkinglotSerializer



class Parkspot(APIView):
    queryset=Parkspot.objects.all()
    serializer_class=ParkspotSerializer

