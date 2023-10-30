# dashboard/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('update-transaction/', update_transaction, name='update_transaction'),
    path('delete-transaction/', delete_transaction, name='delete_transaction'),
]
