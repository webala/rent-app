from django import forms
from .models import House

class CreateHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['number', 'tenant', 'rent']
