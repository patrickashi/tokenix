from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse

from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages 
from django.contrib.auth import authenticate, login

from .models import Profile
from .models import Student
from .models import Notification
from .models import Feedback
from .models import BTC, DASH, Ethereum
from .models import Invest


from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, StudentProfileForm
from .forms import FeedbackForm
from .forms import StudentUpdateForm
from .forms import InvestForm

import csv

import requests
from django.conf import settings
from django.views.generic import View

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
        profile_form = StudentProfileForm()
    return render(request, 'dashboard/register.html', {
        'form': form,
        'profile_form': profile_form
    })



def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Correct field name for password
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard page
            else:
                form.add_error(None, 'Invalid username or password.')  # Add error if authentication fails
        else:
            form.add_error(None, 'Invalid username or password.')  # Add error if form is invalid
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})


@login_required
# feedback
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('dashboard')  # Redirect to the dashboard after submitting feedback
    else:
        form = FeedbackForm()
    return render(request, 'dashboard/submit_feedback.html', {'form': form})

@login_required
def user_feedback(request):
    user_feedbacks = Feedback.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/view_feedback.html', {'feedbacks': user_feedbacks})


@login_required
def dashboard(request):
    # Get the current user's balances for each cryptocurrency
    btc_balance = BTC.objects.filter(user=request.user).first()
    dash_balance = DASH.objects.filter(user=request.user).first()
    ethereum_balance = Ethereum.objects.filter(user=request.user).first()

    firstname = request.user.first_name
    username = request.user.username  # Get the username of the logged-in user
    try:
        student = Student.objects.get(user=request.user)
    except Profile.DoesNotExist:
        student = None  # or handle this case appropriately
        
        
    context = { 'username': username,
                'firstname': firstname,
                'student': student,
                'btc_balance': btc_balance.balance if btc_balance else 0,
                'dash_balance': dash_balance.balance if dash_balance else 0,
                'ethereum_balance': ethereum_balance.balance if ethereum_balance else 0,}
    return render(request, 'dashboard/dashboard.html', context)


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))  # Redirect to the profile page
    else:
        form = StudentRegistrationForm()
    return render(request, 'dashboard/register_student.html', {'form': form})

@login_required
def profile(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, 'Profile does not exist.')
        return redirect('dashboard')  # Redirect to the dashboard or another appropriate page
    
    if request.method == 'POST':
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=request.user.student)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = StudentProfileForm(instance=request.user.student)
        
    
    
    context = {'student': student, 'profile_form': profile_form}
    return render(request, 'dashboard/profile.html', context)  # Ensure this path is correct


@login_required
def update_profile(request):
    student_profile, created = Student.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentUpdateForm(instance=student_profile)
    return render(request, 'dashboard/update_profile.html', {'form': form})


def student_subject_view (request):
    favourite_subject = Student.objects.get('favourite_subject')
    return render(request, 'dashboard/profile.html', {'favourite_subject' : favourite_subject})

#notifications
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    unread_count = notifications.filter(read=False).count()
    context = {
        "notifications": notifications,
        "unread_count": unread_count
    }
    return render(request, "dashboard/notifications.html", context)

def unread_notifications(request):
    unread_notifications = Notification.objects.filter(read=False)
    context = {'unread_notifications': unread_notifications}
    return render(request, 'dashboard/notifications.html', context)

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return redirect("notifications")

def get_unread_notification_count(request):
    unread_count = Notification.objects.filter(user=request.user, read=False).count()
    return JsonResponse({'unread_count': unread_count})


# Only allow admin users to access this view
def admin_required(user):
    return user.is_superuser

@login_required
# @user_passes_test(is_admin)
def send_notification(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")
        users = User.objects.all()
        for user in users:
            Notification.objects.create(user=user, title=title, message=message)
        return redirect("notifications")

    return render(request, "dashboard/send_notification.html")

def invest_page(request):
    if request.method == 'POST':
        form = InvestForm(request.POST)
        if form.is_valid():
            invest = form.save(commit=False)
            invest.user = request.user

            # Validate spent amount based on selected plan
            error_message = None
            profit_percentage = None

            if invest.plan == 'standard':
                if not (10000 <= invest.spent_amount <= 49999):
                    error_message = 'Invalid spent amount for the Standard Plan.'
                else:
                    profit_percentage = 18.00
            elif invest.plan == 'expert':
                if not (50000 <= invest.spent_amount <= 199999):
                    error_message = 'Invalid spent amount for the Expert Plan.'
                else:
                    profit_percentage = 25.50
            elif invest.plan == 'ultimate':
                if not (200000 <= invest.spent_amount <= 499999):
                    error_message = 'Invalid spent amount for the Ultimate Plan.'
                else:
                    profit_percentage = 32.20
            elif invest.plan == 'long_term':
                if not (500000 <= invest.spent_amount <= 500000000):
                    error_message = 'Invalid spent amount for Long Term Investment.'
                else:
                    profit_percentage = 36.00

            # If there's an error, re-render the form with the error message
            if error_message:
                return render(request, 'dashboard/invest_page.html', {
                    'form': form,
                    'error': error_message,
                })

            # Save the profit percentage and the instance
            invest.profit_percentage = profit_percentage
            invest.save()
            
            # Redirect to confirmation page
            return redirect('confirm_deposit', invest_id=invest.id)
    else:
        form = InvestForm()

    return render(request, 'dashboard/invest_page.html', {'form': form})


def confirm_deposit(request, invest_id):
    invest = get_object_or_404(Invest, id=invest_id, user=request.user)
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        if transaction_id:
            invest.transaction_id = transaction_id
            invest.save()
            messages.success(request, "The deposit has been saved. It will become active when the administrator checks statistics.")
            return redirect('invest_page')  # Redirect to dashboard or another page
    return render(request, 'dashboard/confirm_deposit.html', {'invest': invest})
def home(request):
    return render(request, 'home.html')