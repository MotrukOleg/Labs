from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from premier_django.repositories_manager import RepositoryManager
from django_pandas.io import read_frame
from bokeh.layouts import column, gridplot


def graphic1(request):

    data = RepositoryManager.standing.get_percentage_wins()
    df = read_frame(data)
    clubs = df['club'].astype(str).tolist()
    percentage_wins = df['percentage_wins'].tolist()

    p1 = figure(x_range=clubs, height=350, title="Percentage of Wins", toolbar_location=None, tools="")
    p1.vbar(x=clubs, top=percentage_wins, width=0.9)
    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0
    p1.xaxis.major_label_orientation = 1.2

    data2 = RepositoryManager.player_stat.get_top_scorers()
    df2 = read_frame(data2)

    players = df2['player_name_id'].dropna().unique().astype(str).tolist()
    total_goals = df2['total_goals'].tolist()

    p2 = figure(x_range=players, height=350, title="Top Scorers", toolbar_location=None, tools="")
    p2.vbar(x=players, top=total_goals, width=0.9)
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0
    p2.xaxis.major_label_orientation = 1.2

    data3 = RepositoryManager.match_stat.get_high_scoring_matches()
    df3 = read_frame(data3)

    matches = df3['match_id'].dropna().unique().astype(str).tolist()
    total_goals2 = df3['total_goals'].tolist()
    p3 = figure(x_range=matches, height=350, title="High scoring matches", toolbar_location=None, tools="")
    p3.vbar(x=matches, top=total_goals2, width=0.9)
    p3.xgrid.grid_line_color = None
    p3.y_range.start = 0
    p3.xaxis.major_label_orientation = 1.2

    card = RepositoryManager.player_stat.get_cards_stat()
    df4 = read_frame(card)
    player = df4['player_name_id'].dropna().unique().astype(str).tolist()
    yellow_cards = df4['total_yellow'].tolist()
    red_cards = df4['total_red'].tolist()
    p4= figure(x_range=player, height=350, title="Cards Stat", toolbar_location=None, tools="")
    p4.vbar(x=player, top=yellow_cards, width=0.4, color="yellow", legend_label="Yellow Cards")
    p4.vbar(x=player, top=red_cards, width=0.4, color="red", legend_label="Red Cards")
    p4.xgrid.grid_line_color = None
    p4.y_range.start = 0
    p4.xaxis.major_label_orientation = 1.2
    p4.legend.location = "top_left"
    p4.legend.orientation = "horizontal"

    p5 = figure(height=350, title="Cards Stat (Scatter)", toolbar_location=None, tools="")
    p5.scatter(player, yellow_cards, size=8, color="yellow", legend_label="Yellow Cards")
    p5.scatter(player, red_cards, size=8, color="red", legend_label="Red Cards")
    p5.xaxis.major_label_orientation = 1.2
    p5.y_range.start = 0
    p5.legend.location = "top_left"
    p5.legend.orientation = "horizontal"

    cap = RepositoryManager.stadium.get_stadium_capacity()
    df5 = read_frame(cap)
    stad = df5['name'].astype(str).dropna().unique().tolist()
    capacity = df5['capacity'].tolist()
    p6 = figure(x_range=stad, height=350, title="Stadium Capacity", toolbar_location=None, tools="")
    p6.vbar(x=stad  , top=capacity, width=0.9)
    p6.xgrid.grid_line_color = None
    p6.y_range.start = 0
    p6.xaxis.major_label_orientation = 1.2

    club_goals = RepositoryManager.standing.get_avg_goals_by_club()
    df6 = read_frame(club_goals)
    clubs = df6['club'].astype(str).tolist()
    avg_goals = df6['avg_goals'].tolist()

    p7 = figure(x_range=clubs, height=350, title="Average Goals by Club", toolbar_location=None, tools="")
    p7.vbar(x=clubs, top=avg_goals, width=0.9)
    p7.xgrid.grid_line_color = None
    p7.y_range.start = 0
    p7.xaxis.major_label_orientation = 1.2

    layout = column(p1, p2, p3, gridplot([[p4, p5]]), p6 , p7)

    script, div = components(layout)

    return render(request, 'dashboard/dashboardv2.html', {
        'script': script, 'div': div
    })