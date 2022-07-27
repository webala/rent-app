from django import forms
from .models import House, RentRecord, Tenant

class CreateHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['number', 'tenant', 'rent']


class CreateTenant(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone_number']

class CreateRentRecord(forms.ModelForm):
    class Meta:
        model = RentRecord
        fields = ['amount_paid', 'confirmatin_code']