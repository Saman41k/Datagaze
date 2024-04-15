from django.urls import path
from certfication.views import CompanyCertificateView


urlpatterns = [
    path("", CompanyCertificateView.as_view(), name="company_certificate"),
]