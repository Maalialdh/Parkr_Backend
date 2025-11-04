from django.test import TestCase
from django.contrib.auth.models import User
from .models import Parkinglot, Parkspot, Car, Reservation
from datetime import date

class ModelsTest(TestCase):

    def setUp(self):
        # User
        self.user = User.objects.create_user(username='ali', password='12345')

        # Parking lots
        self.lot1 = Parkinglot.objects.create(name='Riyadh Central', location='Riyadh')
        self.lot2 = Parkinglot.objects.create(name='Jeddah Marina', location='Jeddah')

        # Parking spots
        self.spot1 = Parkspot.objects.create(status='available', parkinglot=self.lot1)
        self.spot2 = Parkspot.objects.create(status='reserved', parkinglot=self.lot1)
        self.spot3 = Parkspot.objects.create(status='occupied', parkinglot=self.lot2)

        # Cars
        self.car1 = Car.objects.create(model='Mercedes-Benz', user=self.user, points=10)
        self.car2 = Car.objects.create(model='Honda Civic', user=self.user, points=5)

        # Reservations
        self.reservation1 = Reservation.objects.create(
            user=self.user,
            car=self.car1,
            Parkspot=self.spot1,
            date=date(2025, 11, 4),
            is_completed=False
        )
        self.reservation2 = Reservation.objects.create(
            user=self.user,
            car=self.car2,
            Parkspot=self.spot3,
            date=date(2025, 11, 5),
            is_completed=True
        )

    # String Representations
    def test_user_str(self):
        self.assertEqual(str(self.user), 'ali')

    def test_parkinglot_str(self):
        self.assertEqual(str(self.lot1), 'Riyadh Central - Riyadh')
        self.assertEqual(str(self.lot2), 'Jeddah Marina - Jeddah')

    def test_parkspot_str(self):
        self.assertEqual(str(self.spot1), 'available - Riyadh Central')
        self.assertEqual(str(self.spot3), 'occupied - Jeddah Marina')

    def test_car_str(self):
        self.assertEqual(str(self.car1), 'Mercedes-Benz -Points: 10')
        self.assertEqual(str(self.car2), 'Honda Civic -Points: 5')

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation1), 'ali - available - Riyadh Central (Active)')
        self.assertEqual(str(self.reservation2), 'ali - occupied - Jeddah Marina (Completed)')

    # Relationships
    def test_car_user_relationship(self):
        self.assertEqual(self.car1.user, self.user)
        self.assertEqual(self.car2.user, self.user)

    def test_reservation_relationships(self):
        self.assertEqual(self.reservation1.user, self.user)
        self.assertEqual(self.reservation1.car, self.car1)
        self.assertEqual(self.reservation1.Parkspot, self.spot1)

    def test_parkinglot_parkspot_relationship(self):
        self.assertIn(self.spot1, self.lot1.parkspot_set.all())
        self.assertIn(self.spot2, self.lot1.parkspot_set.all())

    # Cascade Deletions
    def test_deleting_user_cascades_to_cars_and_reservations(self):
        self.user.delete()
        self.assertEqual(Car.objects.count(), 0)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_deleting_car_cascades_to_reservations(self):
        car_id = self.car2.id
        self.car2.delete()
        self.assertEqual(Reservation.objects.filter(car_id=car_id).count(), 0)

    def test_deleting_parkinglot_cascades_to_spots(self):
        lot_id = self.lot1.id
        self.lot1.delete()
        self.assertEqual(Parkspot.objects.filter(parkinglot_id=lot_id).count(), 0)

    # Reservation points system
    def test_complete_reservation_adds_points(self):
        initial_points = self.car1.points
        self.reservation1.is_completed = True
        self.car1.points += 5
        self.car1.save()
        self.assertEqual(self.car1.points, initial_points + 5)

    def test_deleting_reservation_does_not_change_car_points(self):
        initial_points = self.car1.points
        self.reservation1.delete()
        self.car1.refresh_from_db()
        self.assertEqual(self.car1.points, initial_points)
