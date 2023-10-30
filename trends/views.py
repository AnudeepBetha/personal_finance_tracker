from django.shortcuts import render
from dashboard.models import Transaction
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
from collections import defaultdict
from django.db.models import Sum

@login_required
def trends(request):
    current_month = date.today().replace(day=1)
    end_of_month = (current_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Get all transactions for the current month for the user
    transactions = Transaction.objects.filter(
        user_id=request.user,
        date__range=[current_month, end_of_month]
    )

    # Extract unique transaction dates
    transaction_dates = transactions.dates('date', 'day')

    incomes = []
    expenses = []

    # Iterate over unique transaction dates and compute total incomes and expenses for each date
    for transaction_date in transaction_dates:
        daily_incomes = transactions.filter(
            date=transaction_date,
            transaction_type='IN'
        ).aggregate(total=Sum('amount'))['total'] or 0.0

        daily_expenses = transactions.filter(
            date=transaction_date,
            transaction_type='EX'
        ).aggregate(total=Sum('amount'))['total'] or 0.0

        incomes.append(float(daily_incomes))
        expenses.append(float(daily_expenses))

    context = {
        'labels': [day.strftime('%Y-%m-%d') for day in transaction_dates],
        'incomes_data': incomes,
        'expenses_data': expenses,
        'month':     current_month.strftime('%B'),

    }

    return render(request, 'trends/trends.html', context)