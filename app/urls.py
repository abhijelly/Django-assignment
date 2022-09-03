from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("app/register", views.register, name="register"),
    path("app/otp", views.otp, name="otp")
]