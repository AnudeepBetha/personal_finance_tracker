from django.urls import path
from .views import *

urlpatterns = [
    path('', budget, name='budget'),
    path('reports/', reports, name='reports'),
]