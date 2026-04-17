from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Pizza", price=15, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/') # تأكدي من مسار الروابط عندك
        self.assertEqual(response.status_code, 200)