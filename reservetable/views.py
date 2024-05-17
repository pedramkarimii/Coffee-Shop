from django.views.generic import ListView
from .models import Reserve
from typing import Any
from .form import TableNumberForm, DeleteReservationForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.http import HttpResponse
from menu.models import Table
from django.contrib import messages


class ReservedView(ListView, FormView):
    model = Reserve
    template_name = "tablereservation/reservation.html"
    form_class = TableNumberForm

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["mytables"] = Table.objects.filter(
            reserve__user=self.request.user, is_reserved=True
        )
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            table = form.cleaned_data["table_number"]
            table.is_reserved = True
            new_table = Table.objects.get(id=table.id)
            Reserve.objects.create(table=new_table, user=self.request.user)
            table.save()
            messages.success(request, f"{table} table is Reserved for you")
        else:
            return HttpResponse("Error: Form is invalid. Please try again.")
        return redirect("reserve")


class RemoveReservationView(ListView, FormView):
    model = Reserve
    template_name = "tablereservation/removereservations.html"
    form_class = DeleteReservationForm

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["mytables"] = Table.objects.filter(
            reserve__user=self.request.user, is_reserved=True
        )
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            table = form.cleaned_data["table_number"]
            table.is_reserved = False
            new_table = Table.objects.get(id=table.id)
            new_table.delete()
            table.save()
            messages.success(request, f"{table} table is removed for you")
        else:
            return HttpResponse("Error: Form is invalid. Please try again.")
        return redirect("reserve")
