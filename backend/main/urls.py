from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("search/<area>/<crop>/<int:days>", views.search),
    path("detail/<int:id>", views.detail)
]