from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    TRANSACTION_ID = models.AutoField(primary_key=True, editable = False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Income'),
        ('EX', 'Expense'),
    ]
    EXPENSE_TYPE_CHOICES = [
        ('EN', 'Entertainment'),
        ('GR', 'Groceries'),
        ('HO', 'Housing'),
        ('TR', 'Transportation'),
        ('MC', 'Medical Care'),
    ]
    transaction_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
        default='IN',
    )
    expense_type = models.CharField(
        max_length=2,
        choices=EXPENSE_TYPE_CHOICES,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Budget(models.Model):
    id = models.AutoField(primary_key=True, editable = False)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()