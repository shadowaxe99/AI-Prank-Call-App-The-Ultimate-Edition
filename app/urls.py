from django.urls import path
from . import views

urlpatterns = [
    path('make_call/', views.prank_call, name='make_call'),
    path('receive_call/', views.receive_call, name='receive_call'),
]