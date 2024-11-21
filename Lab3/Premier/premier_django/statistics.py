from django.db.models import Avg, Min, Max
from django.http import JsonResponse
from .models import club, match_info, player, player_stats, stadium , goal , assist , standings , club_logo
import pandas as pd

def player_statistic(request):
    stats = player_stats.objects.aggregate(
        Avg_goals=Avg('player_goals'),
        Min_goals=Min('player_goals'),
        Max_goals=Max('player_goals'),
        Median_goals = pd.Series(player_stats.objects.values_list('player_goals', flat=True)).median(),

        Avg_yellow_cards=Avg('player_yellow_cards'),
        Min_yellow_cards=Min('player_yellow_cards'),
        Max_yellow_cards=Max('player_yellow_cards'),
        Median_yellow_cards = pd.Series(player_stats.objects.values_list('player_yellow_cards', flat=True)).median(),

        Avg_red_cards=Avg('player_red_cards'),
        Min_red_cards=Min('player_red_cards'),
        Max_red_cards=Max('player_red_cards'),
        Median_red_cards = pd.Series(player_stats.objects.values_list('player_red_cards', flat=True)).median(),
)
    return JsonResponse(stats)

def club_stats(request):
    stats = standings.objects.aggregate(
        Avg_goals_scored=Avg('goals_scored'),
        Min_goals_scored=Min('goals_scored'),
        Max_goals_scored=Max('goals_scored'),
        Median_goals_scored = pd.Series(standings.objects.values_list('goals_scored', flat=True)).median(),

        Avg_goals_conceded=Avg('goals_conceded'),
        Min_goals_conceded=Min('goals_conceded'),
        Max_goals_conceded=Max('goals_conceded'),
        Median_goals_conceded = pd.Series(standings.objects.values_list('goals_conceded', flat=True)).median(),

        Avg_goal_difference=Avg('goal_difference'),
        Min_goal_difference=Min('goal_difference'),
        Max_goal_difference=Max('goal_difference'),
        Median_goal_difference = pd.Series(standings.objects.values_list('goal_difference', flat=True)).median(),

        Avg_points=Avg('points'),
        Min_points=Min('points'),
        Max_points=Max('points'),
        Median_points = pd.Series(standings.objects.values_list('points', flat=True)).median(),
)
    return JsonResponse(stats)

def grouped_stat(request):
    data = standings.objects.values('club').annotate(avg_points = Avg('points'))
    df = pd.DataFrame(list(data))
    responce_data = {
        "grouped_stat": df.to_dict(orient='records')
    }
    return JsonResponse(responce_data)