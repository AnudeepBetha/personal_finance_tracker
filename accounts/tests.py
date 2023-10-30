from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

# Create your tests here.

class AccountsTestCase(TestCase):

    def test_register_new_user(self):
        print("\nTesting Accounts App")
        print("\nRegistration Test")
        # Simulating a user registration process
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'mobile_number': '1234567890',
            'password1': 'Securepassword@123',
            'password2': 'Securepassword@123',
        })
        
        # Ensuring the user was created
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'testuser')
        
        # Ensuring the UserProfile was created
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.first().mobile_number, '1234567890')

    def test_login_user(self):
        
        print("\nLogin Test")
        # Creating a test user
        User.objects.create_user('testuser', 'testuser@example.com', 'Securepassword@123')
        
        # Simulating a user login process
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Securepassword@123'
        })
        
        # Verifying the user is authenticated
        user = self.client.session.get('_auth_user_id')
        self.assertIsNotNone(user)

    def test_logout_user(self):
        print("\nLogout Test")
        User.objects.create_user('testuser', 'testuser@example.com', 'Securepassword@123')
        self.client.login(username='testuser', password='Securepassword@123')
        self.client.get(reverse('logout'))
        user = self.client.session.get('_auth_user_id')
        self.assertIsNone(user)
