from viewStats.views import landingPage
from django.urls import path

urlpatterns = [
    path('', landingPage)
]