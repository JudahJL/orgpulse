from django.contrib import admin
from .models import User, Donor, Recipient

admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)
