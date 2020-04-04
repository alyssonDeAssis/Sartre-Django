from django.urls import path
from .views import home, spt

urlpatterns = [
    path('', home, name="home"),
    path('spt', spt, name="spt"),
]