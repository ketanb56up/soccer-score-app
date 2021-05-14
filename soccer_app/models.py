import uuid
from django.db import models


class Team(models.Model):
    team_name = models.CharField('Team Name', max_length=30, unique=True)

    def __str__(self):
        return f"{self.team_name}"


class Player(models.Model):
    player_name = models.CharField(max_length=255)
    player_team = models.ManyToManyField(Team)

    def __str__(self):
        return f"{self.player_name}"


class Match(models.Model):
    TEAM_CHOICES =(
        ("onevsone", "1vs1"),
        ("twovstwo", "2vs2"),
        ("onevstwo", "1vs2"),
        ("threevsthree", "3vs3"),
    )

    matchtype = models.CharField(verbose_name ='Match Type', max_length = 30, choices = TEAM_CHOICES, default = '', blank=True)
    first_team_name = models.ManyToManyField(Team, verbose_name='Team1 Name', related_name = 'first_team_name')
    second_team_name = models.ManyToManyField(Team, verbose_name='Team2 Name', related_name = 'second_team_name')


class Rank(models.Model):
    RANKING_CHOICES =(
        ("won", "2"),
        ("draw", "1"),
        ("lost", "0"),
    )

    match_result = models.CharField(verbose_name ='Match Result', max_length = 30, choices = RANKING_CHOICES, default = '', blank=True)
    team = models.ForeignKey(Team ,on_delete=models.SET_DEFAULT, default=1)
    player = models.ForeignKey(Player ,on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.match_result}"


class Summary(models.Model):
    team = models.ForeignKey(Team ,on_delete=models.SET_DEFAULT, default=1)
    game_played = models.IntegerField()
    total_points_scored = models.IntegerField()
    total_close_victories = models.IntegerField()

    def __str__(self):
        return f"{self.team}"
