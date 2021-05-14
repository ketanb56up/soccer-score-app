from django.shortcuts import render
from django.views.generic import View
from soccer_app.models import Rank, Team, Player, Match, Summary
from soccer_app.forms import RankForm, PlayerForm, MatchForm, TeamForm
from soccer_app.forms import PlayerFormset, TeamFormset, RankFormSet
from django.shortcuts import redirect


class TeamView(View):

    def get(self, request):
        # matchform = MatchForm()
        teamformset = TeamFormset()
        return render(request, 'create_team.html', {'teamformset': teamformset})
    
    def post(self, request):
        teamformset = TeamFormset(request.POST)
        for team_form in teamformset:
            if team_form.is_valid():
                team = team_form.save()

        if teamformset.is_valid():
            return redirect('match')
        return render(request, 'create_team.html', {'teamformset': teamformset})


class MatchView(View):

    def get(self, request):
        matchform = MatchForm()
        return render(request, 'create_match.html', {'matchform': matchform})
    
    def post(self, request):
        matchform = MatchForm(request.POST)
        if matchform.is_valid():
            matchform.save()
            return redirect('player')
        return render(request, 'create_match.html', {'matchform': matchform})


class PlayerView(View):

    def get(self, request):
        playerformset = PlayerFormset()
        return render(request, 'create_player.html', {'playerformset': playerformset})
    
    def post(self, request):
        playerformset = PlayerFormset(request.POST)
        for player_form in playerformset:
            if player_form.is_valid():
                player = player_form.save()

        if playerformset.is_valid():
            return redirect('rank')
        return render(request, 'create_player.html', {'playerformset': playerformset})


class RankView(View):

    def get(self, request):
        rankformset = RankFormSet()
        return render(request, 'rank.html', {'rankformset': rankformset})
    
    def post(self, request):
        rankformset = RankFormSet(request.POST)
        for rank_form in rankformset:
            if rank_form.is_valid():
                rank = rank_form.save()

        if rankformset.is_valid():
            return redirect('index')
        return render(request, 'rank.html', {'rankformset': rankformset})


class SummaryView(View):
    def get(self, request):
        summary = Summary.objects.all()
        return render(request, 'summary.html', {'summary': summary})


class IndexView(View):
    def get(self, request):
        teams = Team.objects.all()
        context = []
        for team in teams:
            team1_matchs = Match.objects.filter(first_team_name=team.id)
            team2_matchs = Match.objects.filter(second_team_name=team.id)
            players = team.player_set.all()
            ranks = team.rank_set.all()
            context.append({
                'team':team,
                'players':players,
                'ranks': ranks,
                'team1_matchs': team1_matchs,
                'team2_matchs':team2_matchs,
                }
            )
        return render(request, 'index.html', {'context': context})
