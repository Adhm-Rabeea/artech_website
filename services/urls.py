from django.urls import path
from . import views

urlpatterns = [
    path("", views.our_services, name="our services"),
]
