from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Parkinglot, Parkspot, Car, Reservation

from .serializers import (
    ParkinglotSerializer,
    ParkspotSerializer,
    CarSerializer,
    ReservationSerializer,
    UserSerializer,
)
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                {"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LoginView(APIView):

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                content = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                }
                return Response(content, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as err:
            return Response(
                {"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            try:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": UserSerializer(user).data,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as token_error:
                return Response(
                    {"detail": "Failed to generate token.", "error": str(token_error)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as err:
            return Response(
                {"detail": "Unexpected error occurred.", "error": str(err)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class Home(APIView):
    def get(self, request):
        content = {"message": "Welcome to the Parkr api home route!"}
        return Response(content)


class ParkinglotIndex(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Parkinglot.objects.all()
    serializer_class = ParkinglotSerializer


class ParkspotIndex(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Parkspot.objects.all()
    serializer_class = ParkspotSerializer


class CarIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request):
        try:
            data = request.data.copy()
            data["user"] = int(request.user.id)
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                print(request.user)
                serializer.save(user_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(
                {"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CarDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer

    def get_object(self, car_id, user):
        return get_object_or_404(Car, id=car_id, user=user)

    def get(self, request, car_id):
        car = self.get_object(car_id, request.user)
        serializer = self.serializer_class(car)
        return Response(serializer.data)

    def put(self, request, car_id):
        car = self.get_object(car_id, request.user)
        serializer = self.serializer_class(car, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id):
        car = self.get_object(car_id, request.user)
        car.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)


class ReservationViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_object(self, reservation_id):
        try:
            return Reservation.objects.get(id=reservation_id, user=self.request.user)
        except Reservation.DoesNotExist:
            raise Response(
                {"detail": "Reservation not found."}, status=status.HTTP_404_NOT_FOUND
            )

    # post delete eidt
    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user)
        serializer = self.serializer_class(reservations, many=True)
        #print(serializer.data)
        return Response(serializer.data)

    # إضافة حجز جديد
    def post(self, request):
        data = request.data.copy()
        data["user"] = int(request.user.id)
        data["Parkspot"] = request.data["spot_number"]
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  تعديل الحجز
    def put(self, request, reservation_id):
        reservation = self.get_object(reservation_id)
        serializer = self.serializer_class(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # حذف الحجز
    def delete(self, request, reservation_id):
        reservation = self.get_object(reservation_id)
        reservation.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
    

class CompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, reservation_id):
        try:
            reservation = Reservation.objects.get(id=reservation_id, user=request.user)
            if reservation.is_completed:
                return Response(
                    {"message": "Reservation already completed."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            
            car = reservation.car
            car.points += 5
            car.save()

            reservation.is_completed = True
            reservation.save()

            return Response(
                {
                    "message": f"Reservation completed! 5 points added to {car.model}.",
                    "new_points": car.points,
                },
                status=status.HTTP_200_OK,
            )
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND
            )
