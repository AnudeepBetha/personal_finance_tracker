from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm, ExpenseForm
from dashboard.models import Transaction
from django.http import JsonResponse
import json

@login_required
def financials(request):
    if request.method == 'POST':
        if 'income_form' in request.POST:
            form = IncomeForm(request.POST, prefix='income')
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user_id = request.user
                instance.transaction_type = 'IN'
                instance.save()
                if 'add_multiple' not in request.POST:
                    return redirect('dashboard')
        elif 'expense_form' in request.POST:
            form = ExpenseForm(request.POST, prefix='expense')
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user_id = request.user
                instance.transaction_type = 'EX'
                instance.save()
                if 'add_multiple' not in request.POST:
                    return redirect('dashboard')

    income_form = IncomeForm(prefix='income')
    expense_form = ExpenseForm(prefix='expense')

    return render(request, 'financials/financials.html', {
        'income_form': income_form, 
        'expense_form': expense_form
    })
