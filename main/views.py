from django.shortcuts import render
from .forms import CreateHouse

# Create your views here.


def dash(request):
    return render(request, 'dash.html')

def create_house(request):
    create_house_form = CreateHouse(request.POST or None)

    if create_house_form.is_valid():
        create_house_form.save()
        create_house_form = CreateHouse()

    
    context = {
        'create_house_form': create_house_form
    }

    return render(request, 'create_house.html', context)



