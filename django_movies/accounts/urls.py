from sys import path

from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]