from stats import views
from django.urls import path

urlpatterns = [
    # Teams - GET request
    path('teams', views.getTeams),

    # Matches - GET request
    path('matches', views.getMatches),

    # Players - GET request
    path('players', views.getPlayers),

    # Live Stats - UPDATE request
    path('live/<int:id>', views.updateMatch),

    # Empty path returns endpoint information - GET request
    path('', views.getRoutes),
]
# this is shit code by vinnie
# PENIs was here