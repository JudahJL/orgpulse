from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

from organ_donor.forms import UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from organ_donor.models import Donor, Recipient, OrgPulseAdmin  # Ensure you import your models
from organ_donor.forms import DonorForm, RecipientForm


@login_required
def register_donor(request):
    donor = Donor.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = DonorForm(request.POST, request.FILES, instance=donor)
        if form.is_valid():
            donor_temp = form.save(commit=False)
            donor_temp.user = request.user
            donor_temp.save()

            if donor:
                messages.info(request, "Donor details updated successfully")
            else:
                messages.success(request, "Donor successfully registered")
    else:
        form = DonorForm(instance=donor)

    return render(request, 'donor_register.html', {'form': form})


@login_required
def register_recipient(request):
    recipient = Recipient.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = RecipientForm(request.POST, request.FILES, instance=recipient)
        if form.is_valid():
            recipient_temp = form.save(commit=False)
            recipient_temp.user = request.user
            recipient_temp.save()
            if recipient:
                messages.success(request, "Recipient successfully registered")
            else:
                messages.info(request, "Recipient details updated successfully")
    else:
        form = RecipientForm(instance=recipient)

    return render(request, 'recipient_register.html', {'form': form})


@login_required
def match_donors(request):
    org_pulse_admin = OrgPulseAdmin.objects.filter(user=request.user).first()
    if not org_pulse_admin:
        return redirect('index')

    recipients = Recipient.objects.all()
    matches = []

    for recipient in recipients:
        donor = Donor.objects.filter(
            blood_type=recipient.blood_type,
            organ_type=recipient.organ_type,
            is_available=True
        ).exclude(user=request.user).first()  # Ensure admin is not the donor

        if donor:
            matches.append({'recipient_id': recipient.id, 'recipient_name': recipient.user.username,
                            'donor_id': donor.id, 'donor_name': donor.user.username})

    return render(request, 'match_results.html', {'matches': matches})


@login_required
@require_POST
def send_match_email(request):
    recipient_id = request.POST.get('recipient_id')
    donor_id = request.POST.get('donor_id')

    try:
        recipient = Recipient.objects.get(id=recipient_id)
        donor = Donor.objects.get(id=donor_id, is_available=True)

        if donor.user == request.user:
            return JsonResponse({'error': "Admin cannot approve their own match"}, status=403)

        donor.is_available = False
        donor.save()

        send_mail(
            "Organ Donation Match Found",
            f"Dear {recipient.user.username}, you have been matched.",
            "orgpulse.organ@gmail.com",
            [recipient.user.email],
        )
        send_mail(
            "Organ Donation Match Found",
            f"Dear {donor.user.username}, you have been matched.",
            "orgpulse.organ@gmail.com",
            [donor.user.email],
        )

        return JsonResponse({'success': "Emails sent successfully"})
    except (Recipient.DoesNotExist, Donor.DoesNotExist):
        return JsonResponse({'error': "Invalid recipient or donor"}, status=400)


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


@login_required
def request_admin(request):
    user = request.user
    org_pulse_admin = OrgPulseAdmin.objects.filter(user=user)
    if org_pulse_admin.exists() and org_pulse_admin.first().is_valid == True:
        return redirect('match_donors')

    if request.method == "POST":
        OrgPulseAdmin.objects.create(user=user)
        return redirect('index')

    return render(request, 'Admin.html', {'org_pulse_admin': org_pulse_admin})
