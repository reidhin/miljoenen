from django.urls import path
from nota import views

urlpatterns = [
    path('', views.index, name="index")
]