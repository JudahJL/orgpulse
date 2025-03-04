from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Diseases(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Donor(models.Model):
    BLOOD_TYPES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )
    ORGAN_TYPES = (
        ("Heart", "Heart"),
        ("Lungs", "Lungs"),
        ("Kidney", "Kidney"),
        ("Liver", "Liver"),
        ("Pancreas", "Pancreas"),
        ("Small Intestine", "Small Intestine"),
        ("Eyes", "Eyes"),
    )
    GENDER_TYPES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    organ_type = models.CharField(max_length=50, choices=ORGAN_TYPES)
    address = models.CharField(verbose_name="Address", max_length=100)
    is_available = models.BooleanField(default=True)
    gender = models.CharField(verbose_name="Gender", max_length=10, choices=GENDER_TYPES)
    dob = models.DateField(verbose_name='D.O.B', auto_now_add=False, auto_now=False)
    profile_pic = models.ImageField(upload_to="profile_pics/")
    medical_report = models.ImageField(upload_to="medical_reports/")
    witness_name = models.CharField(verbose_name="Witness Name", max_length=100)
    witness_whatsappNo = PhoneNumberField()
    contact_number = PhoneNumberField(verbose_name="Contact Number")
    whatsappNo = PhoneNumberField()
    diseases = models.ManyToManyField(Diseases, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.organ_type}"


class Recipient(models.Model):
    BLOOD_TYPES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )
    ORGAN_TYPES = (
        ("Heart", "Heart"),
        ("Lungs", "Lungs"),
        ("Kidney", "Kidney"),
        ("Liver", "Liver"),
        ("Pancreas", "Pancreas"),
        ("Small Intestine", "Small Intestine"),
        ("Eyes", "Eyes"),
    )
    GENDER_TYPES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    organ_type = models.CharField(max_length=50, choices=ORGAN_TYPES)
    address = models.CharField(verbose_name="Address", max_length=100)
    is_available = models.BooleanField(default=True)
    gender = models.CharField(verbose_name="Gender", max_length=10, choices=GENDER_TYPES)
    dob = models.DateField(verbose_name='D.O.B', auto_now_add=False, auto_now=False)
    profile_pic = models.ImageField(upload_to="profile_pics/")
    medical_report = models.ImageField(upload_to="medical_reports/")
    witness_name = models.CharField(verbose_name="Witness Name", max_length=100)
    witness_whatsappNo = PhoneNumberField()
    contact_number = PhoneNumberField(verbose_name="Contact Number")
    whatsappNo = PhoneNumberField()
    diseases = models.ManyToManyField(Diseases, blank=True)

    def __str__(self):
        return f"{self.user.username} - Needs {self.organ_type}"
