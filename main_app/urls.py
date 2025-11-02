from django.urls import path
from .views import Home,CarIndex, CarDetail,CreateUserView,LoginView,VerifyUserView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cars/', CarIndex.as_view(), name='car-index'),
    path('cars/<int:car_id>/', CarDetail.as_view(), name='car-detail'),
    # path('reservations/', ReservationViewSet.as_view(), name='reservation-viewset'),
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),



]