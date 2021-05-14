from django import forms
from django.forms import formset_factory
from soccer_app.models import Rank, Team, Player, Match


class RankForm(forms.ModelForm):

    class Meta:
        model = Rank
        fields = "__all__"

RankFormSet = formset_factory(RankForm, extra=1)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = "__all__"

TeamFormset = formset_factory(TeamForm, extra=1)


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = "__all__"

PlayerFormset = formset_factory(PlayerForm, extra=1)


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = "__all__"
