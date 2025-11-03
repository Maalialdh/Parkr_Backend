from django.urls import path
from .views import (
    Home,
    CarIndex,
    ReservationViewSet,
    CarDetail,
    CreateUserView,
    LoginView,
    VerifyUserView,
    AddCarPointsView
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("cars/", CarIndex.as_view(), name="car-index"),
    path("cars/<int:car_id>/", CarDetail.as_view(), name="car-detail"),
    path("reservations/", ReservationViewSet.as_view(), name="reservation-viewset"),
    path("reservations/<int:reservation_id>/", ReservationViewSet.as_view()),
    # path('reservations/<int:pk>/leave/',leave_reservation, name='leave_reservation'),
    path("cars/<int:car_id>/add_points/", AddCarPointsView.as_view(), name="add-car-points"),

    path("users/signup/", CreateUserView.as_view(), name="signup"),
    path("users/login/", LoginView.as_view(), name="login"),
    path("users/token/refresh/", VerifyUserView.as_view(), name="token_refresh"),
]
