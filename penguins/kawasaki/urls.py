from django.urls import path
from .views import view_kawasaki

urlpatterns = [
    path("", view_kawasaki, name="kawasaki"),
]