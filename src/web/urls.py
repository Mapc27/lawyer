from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name="main_view"),
    path('in-developing/', views.in_developing_view, name="in_developing_view"),
]
