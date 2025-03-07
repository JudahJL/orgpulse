from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path
from organ_donor import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/donor/', views.register_donor, name='register_donor'),
    path('register/recipient/', views.register_recipient, name='register_recipient'),
    path('match/', views.match_donors, name='match_donors'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path('', views.index, name='index'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('request_for_admin/', views.request_admin, name='request_for_admin'),
    path('send_match_email/', views.send_match_email, name='send_match_email'),
]
