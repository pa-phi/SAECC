from django.urls import path
from . import views

# URLConf
urlpatterns = [
  path('main', views.say_hello)
]