from django.db import IntegrityError
from django.shortcuts import redirect
from django.core.mail import send_mail
from .forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import Donor, Recipient  # Ensure you import your models
from .forms import DonorForm, RecipientForm


@login_required
def register_donor(request):
    try:
        donor, created = Donor.objects.get_or_create(user=request.user)  # Fetch existing or create new

        if request.method == "POST":
            form = DonorForm(request.POST, request.FILES, instance=donor)
            if form.is_valid():
                form.save()
                if created:
                    messages.success(request, "Donor Successfully registered")
                else:
                    messages.info(request, "Donor details updated successfully")
        else:
            form = DonorForm(instance=donor)

        return render(request, 'donor_register.html', {'form': form})
    except IntegrityError:
        return render(request, 'donor_register.html', {'form': DonorForm()})


@login_required
def register_recipient(request):
    try:
        recipient, created = Recipient.objects.get_or_create(user=request.user)  # Fetch existing or create new

        if request.method == "POST":
            form = RecipientForm(request.POST, instance=recipient)
            if form.is_valid():
                form.save()
                if created:
                    messages.success(request, "Recipient successfully registered")
                else:
                    messages.info(request, "Recipient details updated successfully")
        else:
            form = RecipientForm(instance=recipient)

        return render(request, 'recipient_register.html', {'form': form})
    except IntegrityError:
        return render(request, 'recipient_register.html', {'form': RecipientForm()})


@login_required
def match_donors(request):
    recipients = Recipient.objects.all()
    matches = []

    for recipient in recipients:
        donor = Donor.objects.filter(blood_type=recipient.blood_type, organ_type=recipient.organ_type,
                                     is_available=True).first()
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
