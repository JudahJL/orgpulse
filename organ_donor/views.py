from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UserRegistrationForm, DonorForm, RecipientForm
from .models import Donor, Recipient


@login_required
def register_donor(request):
    if request.method == "POST":
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            messages.success(request, "Donor Successfully registered")
    else:
        form = DonorForm()
    return render(request, 'donor_register.html', {'form': form})


@login_required
def register_recipient(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient.save()
            messages.success(request, "Recipient successfully registered")
    else:
        form = RecipientForm()
    return render(request, 'recipient_register.html', {'form': form})


@login_required
def match_donors(request):
    recipients = Recipient.objects.all()
    matches = []

    for recipient in recipients:
        donor = Donor.objects.filter(blood_type=recipient.blood_type, organ_type=recipient.organ_type, is_available=True).first()
        if donor:
            matches.append((recipient, donor))
            donor.is_available = False
            donor.save()

            # Send email to donor and recipient
            send_mail(
                "Organ Donation Match Found",
                f"Dear {donor.user.username}, you have been matched with {recipient.user.username}.",
                "orgpulse.organ@gmail.com",
                [donor.user.email, recipient.user.email],
            )

    return render(request, 'match_results.html', {'matches': matches})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {'form': form})


def index(request):
    return render(request, 'OrganDonation_home.html')


def contact_us(request):
    return render(request, 'ContactUs.html')