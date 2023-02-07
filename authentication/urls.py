from django.urls import path

from authentication.views.signup import RegistrationView

urlpatterns = [
    path('signup/',RegistrationView.as_view(),name='registration_view')
]