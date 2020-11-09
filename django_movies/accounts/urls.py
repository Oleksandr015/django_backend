from sys import path

from django.contrib.auth.views import LoginView

from accounts.views import SuccessMessagedLogoutView, SubmittablePasswordChangeView



app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('login/', SubmittablePasswordChangeView(), name='password_change'),
]