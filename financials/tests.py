from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Transaction

class FinancialsTestCase(TestCase):

    def setUp(self):
        
        print("\nTesting Financials App")
        
        # Creates a test user for simulation
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        # Initializes the client
        self.client = Client()

    def test_add_income(self):
        print("\nAdd Income Test")
        # Logs in the test user
        self.client.login(username='testuser', password='testpass')
        
        # Defines the test data
        income_data = {
            'income-amount': '500.00',
            'income-date': '2023-10-15',
            'income_form': '', 
        }

        # POST Request
        response = self.client.post(reverse('financials'), income_data)
        
        # Checks if transaction is added successfully, then a redirect would occur
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(Transaction.objects.filter(amount=500.00, transaction_type='IN').exists())

    def test_add_expense(self):
        print("\nAdd Expense Test")
        # Logs in the test user
        self.client.login(username='testuser', password='testpass')
        
        # Defines the data for the expense transaction
        expense_data = {
            'expense-amount': '300.00',
            'expense-date': '2023-10-15',
            'expense-category': 'GR',
            'expense_form': '',
        }

        # Sends a POST request to save the expense transaction
        response = self.client.post(reverse('financials'), expense_data)
        
        # Checks if transaction is added successfully, then a redirect would occur
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Transaction.objects.filter(amount=300.00, transaction_type='EX').exists())