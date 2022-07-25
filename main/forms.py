from django import forms
from .models import House, Tenant

class CreateHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['number', 'tenant', 'rent']


class CreateTenant(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone_number']