from pages.views import mainPage
from django.urls import path

urlpatterns = [
    path('', mainPage),
]