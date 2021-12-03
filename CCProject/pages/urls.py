from pages.views import mainPage, testPage
from django.urls import path

urlpatterns = [
    path('test/', testPage),
    path('', mainPage),
]