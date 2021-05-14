from django.contrib import admin
from soccer_app.models import Team, Player, Match, Rank

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Rank)
