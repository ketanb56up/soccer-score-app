from django.conf.urls import url
from soccer_app.views import (
	IndexView,
	TeamView,
	MatchView,
	PlayerView,
	RankView,
	SummaryView
)

urlpatterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
    url(r'^team/', TeamView.as_view(), name='team'),
    url(r'^match/', MatchView.as_view(), name='match'),
    url(r'^player/', PlayerView.as_view(), name='player'),
    url(r'^rank/', RankView.as_view(), name='rank'),
    url(r'^summary/', SummaryView.as_view(), name='summary'),
]