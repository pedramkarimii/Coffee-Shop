from django.urls import path
from apps.core.views import AboutUsView


urlpatterns = [
    path('aboutus/', AboutUsView.as_view(), name='AboutUs'),
]
