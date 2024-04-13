from django.urls import path 
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  path('register', views.RegisterUserView.as_view()),
  path('verify-email', views.VerifyEmailView.as_view()),
  path ('login', views.LoginApiView.as_view()),
  path ('checkAuth', views.TestAuthenticationView.as_view()),
  path ('reset-password', views.PasswordResetView.as_view(),  name='reset-password'),
  path ('reset-password-confirm/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name='reset-password-confirm'),
  path ('set-new-password', views.SetNewPassword.as_view(), name='set-new-password'),
  path('logout', views.LogoutView.as_view()),
  path('refresh', TokenRefreshView.as_view())
]