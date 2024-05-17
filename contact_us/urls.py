from django.urls import path
from .views import ContactFormView, thank_you

urlpatterns = [
    path("contactus/", ContactFormView.as_view(), name="contact_form"),
    path("thank-you/", thank_you, name="thank_you"),
]
