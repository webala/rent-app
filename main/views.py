from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from main.utils import get_balance
from .forms import CreateHouse, CreateRentRecord, CreateTenant
from .models import House, RentRecord, Tenant
from django.contrib import messages

# Create your views here.


def dash(request):

    houses = House.objects.all()
    context = {
        'houses': houses
    }
    return render(request, 'dash.html', context)

def create_house(request):
    create_house_form = CreateHouse(request.POST or None)

    if create_house_form.is_valid():
        create_house_form.save()
        create_house_form = CreateHouse()

    
    context = {
        'create_house_form': create_house_form
    }

    return render(request, 'create_house.html', context)

def create_tenant(request):
    create_tenant_form = CreateTenant(request.POST or None)

    if create_tenant_form.is_valid():
        create_tenant_form.save()
        create_tenant_form = CreateTenant()

    context = {
        'create_tenant_form': create_tenant_form
    }

    return render(request, 'create_tenant.html', context)


def tenants(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants': tenants
    }

    return render(request, 'tenants.html', context)

def house_view(request, house_id):
    house = House.objects.get(id=house_id)
    edit_house_form = CreateHouse(instance=house)
    create_rent_record_form = CreateRentRecord()
    rent_records = RentRecord.objects.filter(house=house)

    if request.method == 'POST':
        edit_house_form = CreateHouse(request.POST)
        if edit_house_form.is_valid():
            edit_house_form.save()
            #send a message to client side to show success or failure.
            messages.add_message(request, messages.SUCCESS, 'House created successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'House creation failed.')

        

    context = {
        'house': house,
        'edit_house_form': edit_house_form,
        'create_rent_record_form': create_rent_record_form,
        'rent_records': rent_records
    }
    return render(request, 'house.html', context)


def house_rent_records(request, house_id):

    rent_records = RentRecord.objects.all()
    #A post request can be sent to this view to create a rent record
    if request.method == 'POST':
        create_rent_record_form = CreateRentRecord(request.POST)
        house = House.objects.get(id=house_id)
        rent = house.rent
        if create_rent_record_form.is_valid():
            obj = create_rent_record_form.save(commit=False)
            amount_paid = create_rent_record_form.cleaned_data['amount_paid']

            #use a utility function to calculate balance based on previous records
            balance = get_balance(house.id, amount_paid)
            obj.house = house
            obj.balance = balance
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Record created successfully')
            return redirect(house_view, house_id=house.id)
        else:
            messages.add_message(request, messages.ERROR, 'Record creation failed')
            return redirect(house_view, house_id=house.id)
    
    context= {
        'rent_records': rent_records
    }

    return render(request, 'rent_records.html', context)
