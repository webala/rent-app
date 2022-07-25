from django.urls import path
from .views import create_house, create_tenant, dash

urlpatterns = [
    path('', dash, name='dash'),
    path('house/create', create_house, name='create_house'),
    path('tenant/create', create_tenant, name='create_tenant')

]