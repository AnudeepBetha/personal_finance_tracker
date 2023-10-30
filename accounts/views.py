from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileUpdateForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Check if UserProfile already exists for the user
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                user_profile.mobile_number = form.cleaned_data['mobile_number']
                user_profile.save()
            
            # Log the user in and redirect to dashboard
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def update_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    
    # Prepopolating the exsting Email and Password
    initial_data = {
        'email': user.email,
        'mobile_number': user_profile.mobile_number
    }
    
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']  # Update the email on the User model
            user.save()
            return redirect('update_profile')
    else:
        form = UserProfileUpdateForm(initial=initial_data, instance=user_profile)
    
    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'username': request.user.username})