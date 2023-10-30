from django.contrib import admin
from .models import Transaction, Budget
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['TRANSACTION_ID', 'user_id', 'transaction_type', 'expense_type', 'amount', 'date']
    list_filter = ['transaction_type', 'expense_type', 'date']
    search_fields = ['TRANSACTION_ID', 'user_id__username', 'amount']

class BudgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'USER_ID', 'goal', 'month']
    list_filter = ['month']
    search_fields = ['id', 'USER_ID__username', 'goal']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Budget, BudgetAdmin)