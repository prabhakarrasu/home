from django.urls import path

from . import views

urlpatterns = [
    path('buildings/', views.list_bulidings, name="buildings"),
    path('houses/', views.list_house, name="houses"),
    path('teneants/', views.list_teneant, name="teneants"),
]
