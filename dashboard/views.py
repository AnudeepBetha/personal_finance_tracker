from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Transaction
from django.http import JsonResponse


# Create your views here.
@login_required
def dashboard(request):
    user_transactions = Transaction.objects.filter(user_id=request.user.id)
    
    context = {'transactions': user_transactions}
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def update_transaction(request):
    if request.method == "POST":
        try:
            TRANSACTION_ID = request.POST.get('id')
            transaction = Transaction.objects.get(TRANSACTION_ID=TRANSACTION_ID)
            transaction.transaction_type = request.POST.get('transaction_type') 
            transaction.category = request.POST.get('category')
            transaction.amount = request.POST.get('amount')
            transaction.date = request.POST.get('date')
            transaction.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)})
        
@login_required
def delete_transaction(request):
    if request.method == "POST":
        try:
            TRANSACTION_ID = request.POST.get('id')
            transaction = Transaction.objects.get(TRANSACTION_ID=TRANSACTION_ID)
            transaction.delete()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)})