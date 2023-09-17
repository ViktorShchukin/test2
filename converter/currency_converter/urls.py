from django.urls import path

from . import views


urlpatterns = [
    path("func", views.func_convert, name="index"),
    path("oop", views.oop_convert, name="opp_convert")
]