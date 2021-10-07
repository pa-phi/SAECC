from django.db import models

class Team(models.Model):
  name = models.CharField(max_length=50)
  wins = models.IntegerField()
  losses = models.IntegerField()

  def __str__(self):
        return self.name

class Player(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name="players", null=True)

  def __str__(self):
    return self.first_name + " " + self.last_name

class Match(models.Model):
  date = models.DateField()
  home = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='home', null=True)
  away = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='away', null=True)
  
  # TODO: Implement scores
  def winning_team(self):
    return self.home

  # TODO: Implement scores
  def losing_team(self):
    return self.away

  def __str__(self):
    return "match"