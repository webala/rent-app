from django.shortcuts import render
from .forms import CreateHouse, CreateRentRecord, CreateTenant
from .models import House

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


def house_view(request, house_id):
    house = House.objects.get(id=house_id)
    edit_house_form = CreateHouse(instance=house)
    create_rent_record_form = CreateRentRecord(request.POST or None)

    if request.method == 'POST':
        edit_house_form = CreateHouse(request.POST)
        if edit_house_form.is_valid():
            edit_house_form.save()

        if create_rent_record_form.is_valid():
            obj = create_rent_record_form.save(commit=False)

    context = {
        'house': house,
        'edit_house_form': edit_house_form,
        'create_rent_record_form': create_rent_record_form
    }
    return render(request, 'house.html', context)
