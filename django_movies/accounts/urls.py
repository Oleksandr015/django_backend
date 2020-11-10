from django.contrib.auth.views import LoginView

from accounts.views import SuccessMessagedLogoutView, SubmittablePasswordChangeView, SubmittableLoginView, SignUpView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('registration/', SignUpView.as_view(), name='registration'),
]
