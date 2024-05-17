from django.urls import path
from .views import ReservedView, RemoveReservationView

urlpatterns = [
    path("reserve/", ReservedView.as_view(), name="reserve"),
    path("removereserve", RemoveReservationView.as_view(), name="deletereserve"),
]
