from django import forms
from django.forms import DateInput
from dashboard.models import Transaction

class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(min_value=0)
    class Meta:
        model = Transaction
        fields = ['amount', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(min_value=0)
    class Meta:
        model = Transaction
        fields = ['expense_type', 'amount', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }