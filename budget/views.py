from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from dashboard.models import Budget, Transaction
from .forms import BudgetForm
from datetime import timedelta, date
from django.db.models import Sum, Q
import json

# Create your views here.

@login_required
def budget(request):
    current_month = date.today().replace(day=1)
    budget = Budget.objects.filter(month=current_month, USER_ID=request.user).first()

    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.instance.USER_ID = request.user
            form.instance.month = current_month
            form.save()
            return redirect('reports')
    else:
        form = BudgetForm(instance=budget)
    
    context = {
        'form': form,
        'month': current_month.strftime('%B'),
    }
    return render(request, 'budget/budget.html', context)


@login_required
def reports(request):
    current_month = date.today().replace(day=1)
    end_of_month = (current_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    weeks_data = []
    for i in range(4):
        start_week = current_month + timedelta(days=i*7)
        end_week = start_week + timedelta(days=6)
        if end_week > end_of_month:
            end_week = end_of_month

        incomes = Transaction.objects.filter(user_id=request.user, 
                                             date__range=[start_week, end_week], 
                                             transaction_type='IN').aggregate(total=Sum('amount'))['total'] or 0
                                             
        expenses = Transaction.objects.filter(user_id=request.user, 
                                              date__range=[start_week, end_week], 
                                              transaction_type='EX').aggregate(total=Sum('amount'))['total'] or 0
                                              
        weeks_data.append({
            'start': start_week.strftime('%Y-%m-%d'),
            'end': end_week.strftime('%Y-%m-%d'),
            'incomes': float(incomes),
            'expenses': float(expenses),
            'savings': float(incomes - expenses)
        })

    monthly_goal = Budget.objects.filter(USER_ID=request.user, month=current_month).first()
    if monthly_goal:
        goal = monthly_goal.goal
    else:
        goal = 0

    context = {
        'weeks_data_json': json.dumps(weeks_data),
        'goal': goal,
        'month': current_month.strftime('%B'),
    }
    return render(request, 'budget/reports.html', context)
