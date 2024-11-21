from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django_pandas.io import read_frame
from premier_django.repositories_manager import RepositoryManager

def interactive_chart(request):
    data = RepositoryManager.player.get_all()
    df = read_frame(data)

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Football Player Stats Dashboard", style={
            'text-align': 'center',
            'font-size': '3rem',
            'color': '#fff',
            'background': 'linear-gradient(45deg, #00b894, #0984e3)',
            'padding': '20px',
            'border-radius': '10px',
            'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.2)',
            'margin-bottom': '30px',
        }),
        html.Div([
            html.P("Home", style={'display': 'inline-block', 'margin-right': '10px'}),
        ], style={
            'background': '#f1f2f6',
            'padding': '10px',
            'border-radius': '10px',
            'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.2)',
            'margin-bottom': '30px',
        }),



        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='age-dropdown',
                    options=[{'label': str(age), 'value': age} for age in sorted(df['age'].unique())] + [
                        {'label': 'Any', 'value': 'Any'}],
                    value='Any',
                    multi=False,
                    placeholder='Select Age',
                    style={
                        'width': '100%',
                        'padding': '10px',
                        'margin-bottom': '20px',
                        'border-radius': '8px',
                        'background-color': '#ffeaa7',
                        'color': '#2d3436',
                        'font-weight': 'bold',
                        'border': '1px solid #dfe6e9',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                    }
                ),
            ], style={'width': '30%', 'padding': '10px', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='price-dropdown',
                    options=[{'label': f"${price:,}", 'value': price} for price in sorted(df['price'].unique())] + [
                        {'label': 'Any', 'value': 'Any'}],
                    value='Any',
                    multi=False,
                    placeholder='Select Price',
                    style={
                        'width': '100%',
                        'padding': '10px',
                        'margin-bottom': '20px',
                        'border-radius': '8px',
                        'background-color': '#fab1a0',
                        'color': '#2d3436',
                        'font-weight': 'bold',
                        'border': '1px solid #dfe6e9',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                    }
                ),
            ], style={'width': '30%', 'padding': '10px', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id='club-dropdown',
                    options=[{'label': club, 'value': club} for club in df['current_club'].unique()] + [
                        {'label': 'Any', 'value': 'Any'}],
                    value='Any',
                    multi=False,
                    placeholder='Select Club',
                    style={
                        'width': '100%',
                        'padding': '10px',
                        'margin-bottom': '20px',
                        'border-radius': '8px',
                        'background-color': '#6c5ce7',
                        'color': '#2d3436',
                        'font-weight': 'bold',
                        'border': '1px solid #dfe6e9',
                        'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                    }
                ),
            ], style={'width': '30%', 'padding': '10px', 'display': 'inline-block'}),

        ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '40px'}),


        html.Div([
            dcc.Graph(
                id='player-graph',
                style={
                    'border-radius': '10px',
                    'box-shadow': '0px 4px 15px rgba(0, 0, 0, 0.1)',
                    'background': '#fff',
                    'border': '1px solid #dfe6e9',
                    'margin-bottom': '40px',
                    'padding': '20px',
                }
            ),
        ]),

        html.Div([
            html.Div(id='player-table', style={
                'padding': '20px',
                'border-radius': '10px',
                'background-color': '#f6e58d',
                'box-shadow': '0px 4px 15px rgba(0, 0, 0, 0.1)',
                'border': '1px solid #dfe6e9',
            }),
        ], style={'margin-top': '40px'})
    ])

    @app.callback(
        [Output('player-graph', 'figure'),
         Output('player-table', 'children')],
        [Input('age-dropdown', 'value'),
         Input('price-dropdown', 'value'),
         Input('club-dropdown', 'value')]
    )
    def update_dashboard(selected_age, selected_price, selected_club , *args , **kwargs):
        filtered_df = df

        if selected_age != 'Any':
            filtered_df = filtered_df[filtered_df['age'] == selected_age]

        if selected_price != 'Any':
            filtered_df = filtered_df[filtered_df['price'] == selected_price]

        if selected_club != 'Any':
            filtered_df = filtered_df[filtered_df['current_club'] == selected_club]

        fig = px.scatter(filtered_df, x='player_name', y='player_stats__player_goals',
                         title='Total Goals Scored by Players',
                         labels={'player_name': 'Player', 'player_stats__player_goals': 'Total Goals'})


        column_to_display = ['player_name','height', 'age', 'price', 'current_club' , 'player_stats__player_goals']
        filtered_df = filtered_df[column_to_display]

        table = html.Table(
            style={'width': '100%', 'border-collapse': 'collapse'},
            children=[
                         html.Tr(
                             style={'background-color': '#f2f2f2'},
                             children=[
                                 html.Th(col,
                                         style={'padding': '8px', 'text-align': 'center', 'border': '1px solid #ddd'})
                                 for col in filtered_df.columns
                             ]
                         )
                     ] +
                     [
                         html.Tr(
                             children=[
                                 html.Td(filtered_df.iloc[i][col],
                                         style={'padding': '8px', 'text-align': 'center', 'border': '1px solid #ddd'})
                                 for col in filtered_df.columns
                             ],
                             style={'background-color': '#f9f9f9' if i % 2 == 0 else 'white'}
                         )
                         for i in range(len(filtered_df))
                     ]
        )

        return fig, table


    app.run_server(debug=True, use_reloader=False)

    return render(request, 'dashboard/interactive_dashboard.html', {'graph': app.index()})
