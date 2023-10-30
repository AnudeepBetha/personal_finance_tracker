from django.test import TestCase, Client
from django.urls import reverse
from dashboard.models import Transaction
from django.contrib.auth.models import User

class DashboardTestCase(TestCase):

    def setUp(self):
        
        print("\nTesting Dashboard App")
        
        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Creating a test transaction
        self.transaction = Transaction.objects.create(
            user_id=self.user,
            transaction_type='IN',
            amount=100.00,
            date="2023-10-10"
        )
        
        # Initializing the test client
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_edit_transaction(self):
        print("\nEdit Transaction Test")
        
        url = reverse('update_transaction')
        
        # Data for updating the transaction
        data = {
            'id': self.transaction.TRANSACTION_ID,
            'amount': 150.00,
            'date': "2023-10-11",
            'transaction_type': 'EX'
        }
        
        # Making a POST request to the update URL
        response = self.client.post(url, data)
        
        # Check if the transaction is updated in the database
        self.transaction.refresh_from_db()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(self.transaction.amount, 150.00)
        self.assertEqual(self.transaction.date.strftime('%Y-%m-%d'), "2023-10-11")
        self.assertEqual(self.transaction.transaction_type, 'EX')

    def test_delete_transaction(self):
        print("\nDelete Transaction Test")
        
        url = reverse('delete_transaction')
        
        # Data for deleting the transaction
        data = {
            'id': self.transaction.TRANSACTION_ID,
        }
        
        # Making a POST request to the delete URL
        response = self.client.post(url, data)
        
        # Check if the transaction is deleted from the database
        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(TRANSACTION_ID=self.transaction.TRANSACTION_ID)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
