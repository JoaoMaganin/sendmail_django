from django.urls import path
from .views import inscrever


urlpatterns = [
    path('', inscrever, name='inscrever'),
]
