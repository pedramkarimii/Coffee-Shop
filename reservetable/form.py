from django import forms
from .models import Reserve
from menu.models import Table


class TableNumberForm(forms.Form):
    table_number = forms.ModelChoiceField(Table.objects.filter(is_reserved=False))


class DeleteReservationForm(forms.Form):
    table_number = forms.ModelChoiceField(Table.objects.filter(is_reserved=True))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(DeleteReservationForm, self).__init__(*args, **kwargs)
        self.fields["table_number"].queryset = Table.objects.filter(
            is_reserved=True, user=self.user
        )
