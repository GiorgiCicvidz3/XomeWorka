from django.urls import path
from .views import view_kago

urlpatterns = [
    path('', view_kago, name='kago')
]
