from django.test import TestCase
from .models import Booking
from datetime import date

class BookingModelTest(TestCase):
    def test_create_booking(self):
        item = Booking.objects.create(
            first_name="Sara", 
            reservation_date=date(2026, 4, 20),
            reservation_slot=12
        )
        
        self.assertEqual(str(item), "Sara")
        self.assertEqual(item.reservation_slot, 12)