from django.urls import path
from .views import create_house, create_tenant, dash, house_view

urlpatterns = [
    path('', dash, name='dash'),
    path('house/create', create_house, name='create_house'),
    path('tenant/create', create_tenant, name='create_tenant'),
    path('house/<int:house_id>', house_view, name='house')
]