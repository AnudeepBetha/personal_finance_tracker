from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "mobile_number", "password1", "password2")
    
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")
        if len(mobile_number) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits long.")
        return mobile_number
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("The password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("The password must contain at least 1 digit.")
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError("The password must contain at least 1 letter.")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("The password must contain at least 1 uppercase letter.")
        if not any(char in '!@#$%^&*()_+' for char in password):
            raise forms.ValidationError("The password must contain at least 1 special character.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 15:
            raise forms.ValidationError("The username must be no more than 15 characters long.")
        return username

class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=10)

    class Meta:
        model = UserProfile
        fields = ("email", "mobile_number")
