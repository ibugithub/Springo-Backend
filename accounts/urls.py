from django.urls import path 
from . import views



urlpatterns = [
  path('register', views.RegisterUserView.as_view(), name='rester'),
  path('verify-email', views.VerifyEmailView.as_view(), name='verifyEmail'),
  path ('login', views.LoginApiView.as_view(), name='login'),
  path ('testAuth', views.TestAuthenticationView.as_view(), name='testAuth'),
  path ('reset-password', views.PasswordResetView.as_view(),  name='reset-password'),
  path ('reset-password-confirm/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name='reset-password-confirm'),
  path ('set-new-password', views.SetNewPassword.as_view(), name='set-new-password'),
  path('logout', views.LogoutView.as_view(), name='Logout')
]