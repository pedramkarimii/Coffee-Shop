from django.urls import path
from .views import AboutUsView


urlpatterns = [
    path('aboutus/', AboutUsView.as_view(), name='AboutUs'),
]
