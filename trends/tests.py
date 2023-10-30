from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TrendsViewTestCase(TestCase):
    
    def setUp(self):
        print("\nTesting Trends App")
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.url = reverse('trends')

    def test_trends_view_for_unauthenticated_user(self):
        print("\nAuthenticated Access to Trends Test")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
