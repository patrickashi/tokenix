from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    favorite_subject = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    # Add any other fields you need

    def __str__(self):
        return self.user.username

    
    
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
     
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True,)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True,)
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username if self.user else 'No User'
    
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'  

    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='No Title')
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

# Abstract base model to share common fields and functionality
class CryptoBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=20, default="0")

    class Meta:
        abstract = True

class BTC(CryptoBase):
    pass

class DASH(CryptoBase):
    pass

class Ethereum(CryptoBase):
    pass

class Invest(models.Model):
    PLAN_CHOICES = [
        ('standard', 'Standard Plan'),
        ('expert', 'Expert Plan'),
        ('ultimate', 'Ultimate Plan'),
        ('long_term', 'Long Term Investment Stacking'),
    ]

    CRYPTO_CHOICES = [
        ('BTC', 'Bitcoin (BTC)'),
        ('ETH', 'Ethereum (ETH)'),
        ('USDT', 'Tether (USDT)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    spent_amount = models.DecimalField(max_digits=15, decimal_places=2)
    crypto = models.CharField(max_length=10, blank=True, null=True, choices=CRYPTO_CHOICES)  # New field
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan} - {self.crypto}"