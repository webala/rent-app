from django.shortcuts import render

# Create your views here.


def dash(request):
    return render(request, 'dash.html')

def create_house(request):
    pass