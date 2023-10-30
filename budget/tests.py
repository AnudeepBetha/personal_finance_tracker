from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Budget

class FinancialsTestCase(TestCase):

    def setUp(self):
        # Creates a test user for Budget App simulation
        print("\nTesting Budget App")
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        # Initializes the client
        self.client = Client()

    def test_add_goal(self):
        print("\nAdding Budget Goal Test")
        # Logs in the test user
        self.client.login(username='testuser', password='testpass')
        
        # Defines the test data
        budget_data = {
            'goal': '500.00',
            'month': '2023-09-01',
            'USER-ID': self.user.id,
        }

        # POST Request
        response = self.client.post(reverse('budget'), budget_data)
        
        # Checks if budget is added successfully, then a redirect would occur
        self.assertEqual(response.status_code, 302)
        
    def test_reports_view_for_unauthenticated_user(self):
            
        print("\nAuthenticated Access to Reports Test")
        url = reverse('reports')

        response = self.client.get(url)
            
        # Checks for a redirect to login, if unauthenticated user is able to view reports
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)