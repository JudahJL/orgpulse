from datetime import datetime, timedelta

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from organ_donor.models import User, Donor, Recipient, Diseases, Category, OrgPulseAdmin


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class DonorForm(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'max': (datetime.today().date() - timedelta(days=18 * 365)).strftime('%Y-%m-%d'),
                'min': (datetime.today().date() - timedelta(days=60 * 365)).strftime('%Y-%m-%d')}
        ),
        required=True
    )

    diseases = forms.ModelMultipleChoiceField(
        queryset=Diseases.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )

    class Meta:
        model = Donor
        fields = ['dob', 'gender', 'whatsappNo', 'blood_type', 'diseases', 'organ_type', 'address', 'profile_pic', 'medical_report', 'witness_name', 'witness_whatsappNo']


class RecipientForm(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'max': (datetime.today().date() - timedelta(days=18 * 365)).strftime('%Y-%m-%d'),
                'min': (datetime.today().date() - timedelta(days=60 * 365)).strftime('%Y-%m-%d')}
        ),
        required=True
    )

    diseases = forms.ModelMultipleChoiceField(
        queryset=Diseases.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Recipient
        fields = ['dob', 'gender', 'whatsappNo', 'blood_type', 'diseases', 'organ_type', 'address', 'profile_pic', 'medical_report', 'witness_name', 'witness_whatsappNo']


class OrgPulseAdminForm(forms.ModelForm):
    verify = forms.BooleanField(required=True)