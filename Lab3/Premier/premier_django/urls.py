from django.urls import path, include
from rest_framework import routers

from premier_django import views, views_plotly, views_bokeh, views_interactive

from .views import ClubViewSet, PlayerViewSet, MatchViewSet, UserViewSet, TopScorersAPIView, PlayerStatsAPIView, \
    ClubStatsAPIView, GroupedStatsAPIView

routers = routers.DefaultRouter()
routers.register(r'clubs', ClubViewSet)
routers.register(r'players', PlayerViewSet)
routers.register(r'matches', MatchViewSet)
routers.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('clubs/', views.club_list, name='club_list'),
    path('clubs/new/', views.club_create, name='club_create'),
    path('clubs/<int:club_id>/edit/', views.club_update, name='club_update'),
    path('clubs/<int:club_id>/delete/', views.club_delete, name='club_delete'),
    path('clubs/<int:club_id>/', views.club_detail , name='club_detail'),

    # Player URLs
    path('players/', views.player_list, name='player_list'),
    path('players/new/', views.player_create, name='player_create'),
    path('players/<int:player_id>/edit/', views.player_update, name='player_update'),
    path('players/<int:player_id>/delete/', views.player_delete, name='player_delete'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),

    # Match URLs
    path('matches/', views.match_list, name='match_list.html'),
    path('matches/new/', views.match_create, name='match_create'),
    path('matches/<int:match_id>/edit/', views.match_update, name='match_update'),
    path('matches/<int:match_id>/delete/', views.match_delete, name='match_delete'),
    path('matches/<int:match_id>/', views.match_detail, name='match_detail'),

    path('player_stats/', views.player_stats_list, name='player_stats_list'),

    path('standings/', views.standings_list, name='standings_list'),

    path('goals/', views.goal_list, name='goal_list'),
    path('goals/new/', views.goal_create, name='goal_create'),
    path('goals/<int:goal_id>/delete/', views.goal_delete, name='goal_delete'),
    path('api/', include(routers.urls)),

    path('api/clubs/<int:pk>/', ClubViewSet.as_view({'get': 'retrieve'})),
    path('api/clubs_create/', ClubViewSet.as_view({'post': 'create'})),
    path('api/clubs_update/<int:pk>/', ClubViewSet.as_view({'put': 'update'})),
    path('api/clubs_delete/<int:pk>/', ClubViewSet.as_view({'delete': 'destroy'})),

    path('api/players/<int:pk>/', PlayerViewSet.as_view({'get': 'retrieve'})),
    path('api/players_create/', PlayerViewSet.as_view({'post': 'create'})),
    path('api/players_update/<int:pk>/', PlayerViewSet.as_view({'put': 'update'})),

    path('api/matches/<int:pk>/', MatchViewSet.as_view({'get': 'retrieve'})),
    path('api/matches_create/', MatchViewSet.as_view({'post': 'create'})),
    path('api/matches_update/<int:pk>/', MatchViewSet.as_view({'put': 'update'})),
    path('api/matches_delete/<int:pk>/', MatchViewSet.as_view({'delete': 'destroy'})),

    path('top_scorers/' , TopScorersAPIView.as_view(), name='top_scorers'),
    path('avg_goals/' , views.AvgGoalsAPIView.as_view(), name='avg_goals'),
    path('top_match_goals/' , views.TopGoalsPerMatchAPIView.as_view() , name='top_match_goals'),
    path('percent_wins/' , views.PercentWinsAPIView.as_view(), name='percent_wins'),
    path('cards_stat/' , views.CardsStatAPIView.as_view(), name='cards_stat'),
    path('capacities/' , views.StadiumCapacityAPIView.as_view(), name='capacities'),

    path('statistics/player/' , PlayerStatsAPIView.as_view(), name='player_statistic'),
    path('statistics/club/' , ClubStatsAPIView.as_view(), name='club_statistics'),
    path('statistics/grouped/' , GroupedStatsAPIView.as_view(), name='grouped_statistics'),

    path('dashboardv1/' , views_plotly.graphic1, name='dashboardv1'),
    path('dashboardv2/' , views_bokeh.graphic1 ,  name='dashboardv2'),
    path('interactive_dashboard/' , views_interactive.interactive_chart , name='interactive_dashboard'),

    path('users/' , views.item_list, name='item_list'),
    path('users/delete/<int:item_id>/', views.delete_item, name='delete_item'),

]