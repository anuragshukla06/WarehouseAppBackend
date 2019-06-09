from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("search/<area>/<fruit>/<int:days>", views.search),
]