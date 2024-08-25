from django.urls import path
from . import views5




urlpatterns = [
    path("", views.say_hello_pintu),
    path("hello/",views.say_hello_world),
]