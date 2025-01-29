from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student
from .models import Profile
from .models import Feedback
from .models import Invest
from .models import Withdrawal
from .models import Contact


# class RegistrationForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

    def save(self, commit=True):
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name

        if commit:
            user.save()

        return user
        
        


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_photo']
        

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'gender', 'nationality',
                 'phone_number', 'email', 'address', 'profile_photo']
        
        
        
        
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text']
        widgets = {
            'feedback_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        
class InvestForm(forms.ModelForm):
    class Meta:
        model = Invest
        fields = ['plan', 'spent_amount', 'crypto']  # Include 'crypto'
        widgets = {
            'plan': forms.RadioSelect,  # Plan as a radio button
            'crypto': forms.Select(attrs={'class': 'form-control'}),  # Crypto as a dropdown
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].choices = [
            ('standard', 'Standard Plan ($10,000 - $49,999, Profit: 18.00%)'),
            ('expert', 'Expert Plan ($50,000 - $199,999, Profit: 25.50%)'),
            ('ultimate', 'Ultimate Plan ($200,000 - $499,999, Profit: 32.20%)'),
            ('long_term', 'Long Term Investment ($500,000 - $500,000,000, Profit: 36.00%)'),
        ]
        self.fields['crypto'].choices = [
            ('BTC', 'Bitcoin (BTC)'),
            ('ETH', 'Ethereum (ETH)'),
            ('USDT', 'Usdt (USDT)'),
        ]

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['amount', 'crypto', 'wallet_address', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message']
