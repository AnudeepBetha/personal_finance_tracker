from django.urls import path
from .views import *

urlpatterns = [
    path('', financials, name='financials'),]
