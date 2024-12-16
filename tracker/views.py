from django.shortcuts import render, redirect
from .models import TrackingHistory, CurrentBalance
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.filter(
            username = username
        )
        if user.exists():
            messages.success(request, "Username already taken")
            return redirect("/register/")
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created")
        return redirect("/")
    return render(request, 'register.html', {'messages': messages})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(
            username = username
        )
        if not user.exists():
            messages.success(request, "Account not found")
            return redirect("/login/")
        user = authenticate(
            username = username,
            password = password
        )
        if not user:
            messages.success(request, "Incorrect password")
            return redirect("/login/")
        
        login(request, user)
        return redirect("/")
    return render(request, 'login.html', {'messages': messages})

def logout_view(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url="login_page")
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        current_balance = CurrentBalance.objects.get_or_create(id=1)
        print(current_balance)
        expense_type = 'CREDIT'
        if float(amount) < 0:
            expense_type = 'DEBIT'
        tracking_history = TrackingHistory.objects.create(
            amount = float(amount),
            description = description,
            expense_type = expense_type,
            current_balance = current_balance[0]
        )
        current_balance[0].current_balance += tracking_history.amount
        current_balance[0].save()
        print(description, amount)
        return redirect("/")
    current_balance = CurrentBalance.objects.get_or_create(id=1)
    income = 0
    expense = 0
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == 'CREDIT':
            income += tracking_history.amount
        else:
            expense += -tracking_history.amount
    context = {'income':income, 'expense': expense,'transactions': TrackingHistory.objects.all(), 'current_balance': current_balance[0].current_balance}
    return render(request, 'index.html', context)

def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)
    if tracking_history.exists():
        tracking_history = tracking_history[0]
        current_balance = CurrentBalance.objects.get_or_create(id=1)[0]
        current_balance.current_balance -= tracking_history.amount
        current_balance.save()
    tracking_history.delete()
    return redirect("/")
