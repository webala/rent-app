from django.urls import path
from .views import create_house, dash

urlpatterns = [
    path('', dash, name='dash'),
     path('house/create', create_house, name='create_house')
]