from django.db import models

class Team(models.Model):
  name = models.CharField(max_length=50)
  wins = models.IntegerField()
  losses = models.IntegerField()

class Player(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

class Match(models.Model):
  date = models.DateField()
  home = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='home', null=True)
  away = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='away', null=True)


