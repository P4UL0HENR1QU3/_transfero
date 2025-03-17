from django.urls import path
from sistema import views

urlpatterns = [
    path('sistema/', views.index),
]