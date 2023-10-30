from django import forms
from dashboard.models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['goal']