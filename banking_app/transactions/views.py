from django.shortcuts import render, redirect
from .models import Transaction
from accounts.models import CustomUser
from decimal import Decimal

def deposit(request):
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        user = request.user
        user.balance += amount
        user.save()
        Transaction.objects.create(user=user, transaction_type='deposit', amount=amount)
        return redirect('balance')
    return render(request, 'transactions/deposit.html')

def withdraw(request):
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        user = request.user
        if user.balance >= amount:
            user.balance -= amount
            user.save()
            Transaction.objects.create(user=user, transaction_type='withdraw', amount=amount)
            return redirect('balance')
        else:
            return render(request, 'transactions/withdraw.html', {'error': 'Insufficient balance.'})
    return render(request, 'transactions/withdraw.html')

def check_balance(request):
    balance = request.user.balance
    return render(request, 'transactions/balance.html', {'balance': balance})
