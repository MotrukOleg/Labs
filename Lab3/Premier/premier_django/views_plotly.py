from cProfile import label
from functools import total_ordering

from bokeh.colors.named import colors
from bokeh.core.property.vectorization import value
from dash import dash, html, dcc
from django.shortcuts import render
from django_pandas.io import read_frame
import plotly.express as px
from plotly.subplots import make_subplots

from premier_django.models import standings
from premier_django.repositories_manager import RepositoryManager

def graphic1(request):
    standings_data = RepositoryManager.standing.get_percentage_wins()
    df = read_frame(standings_data)

    fig = px.bar(
        df,
        x='club',
        y='percentage_wins',
        title='Percentage of wins',
        labels={'percentage_wins': 'Percentage of wins', 'club__name': 'Club'}
    )

    graph = fig.to_html(full_html=False)

    data = RepositoryManager.player_stat.get_top_scorers()
    df = read_frame(data)
    fig = px.pie(
        df,
        names='player_name_id',
        values='total_goals',
        title='Top Scorers',
        labels={'total_goals': 'Total goals', 'player_name_id': 'Player'}
    )
    graph2 = fig.to_html(full_html=False)

    match = RepositoryManager.match_stat.get_high_scoring_matches()
    df = read_frame(match)
    print(df)
    sorteddf = df.sort_values('total_goals')
    print(sorteddf)

    fig = px.bar(
        sorteddf,
        x= 'match_id',
        y= 'total_goals',
        title = 'High scoring matches',
        labels={'total_goals': 'Total goals' , 'match_id':'Match', 'home_team' : 'Home Team', 'away_team' : 'Away team'  }
    )
    graph3 = fig.to_html(full_html = False)

    cards_data = RepositoryManager.player_stat.get_cards_stat()
    df = read_frame(cards_data)


    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=['Yellow Cards', 'Red Cards']
    )


    scatter_fig = px.scatter(df, x='player_name_id', y='total_yellow', title='Yellow Cards')
    fig.add_trace(scatter_fig.data[0], row=1, col=1)


    bar_fig = px.bar(df, x='player_name_id', y='total_red', title='Red Cards')
    fig.add_trace(bar_fig.data[0], row=1, col=2)

    fig.update_traces(marker_color='green', marker_line_width=1, marker_size=8, selector=dict(type='scatter'))
    fig.update_traces(marker_color='gray', marker_line_width=1, selector=dict(type='bar'))



    fig.update_layout(
        title="Player Cards Statistics",
        xaxis_title="Player",
        yaxis_title="Count",
        legend_title="Card Type",
        barmode="group"
    )

    graph4 = fig.to_html(full_html=False)

    cap = RepositoryManager.stadium.get_stadium_capacity()
    df = read_frame(cap)

    fig = px.bar(
        df,
        x='name',
        y='capacity',
        title='Stadium Capacity',
        labels={'capacity': 'Capacity', 'name': 'Stadium'}
    )

    graph5 = fig.to_html(full_html=False)

    club_performance = RepositoryManager.standing.get_avg_goals_by_club()
    df = read_frame(club_performance)
    fig = px.bar(
        df,
        x='club',
        y='avg_goals',
        title='Average goals by club',
        labels={'avg_goals': 'Average goals', 'club__name': 'Club'}
    )
    graph6 = fig.to_html(full_html=False)



    return render(request, 'dashboard/dashboardv1.html', {
        'graph': graph ,
        'graph2': graph2,
        'graph3':graph3,
        'graph4':graph4,
        'graph5':graph5,
        'graph6': graph6})