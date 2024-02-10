from ctypes import alignment
import dash
import base64
import numpy
from PIL import Image
from dash.dependencies import Input, Output
from dash import html, dcc
from nba_api.stats.endpoints import leaguegamefinder
import requests

image_path = 'img.png'

pil_img = Image.open('img.png')

def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

gamefinder = leaguegamefinder.LeagueGameFinder(
    date_from_nullable='10/18/2022', league_id_nullable='00')
games = gamefinder.get_data_frames()[0]

team_list = [
'Atlanta Hawks',
'Boston Celtics',
'Brooklyn Nets',
'Charlotte Hornets',
'Chicago Bulls',
'Cleveland Cavaliers',
'Dallas Mavericks',
'Denver Nuggets',
'Detroit Pistons',
'Golden State Warriors',
'Houston Rockets',
'Indiana Pacers',
'Los Angeles Clippers',
'Los Angeles Lakers',
'Memphis Grizzlies',
'Miami Heat',
'Milwaukee Bucks',
'Minnesota Timberwolves',
'New Orleans Pelicans',
'New York Knicks',
'Oklahoma City Thunder',
'Orlando Magic',
'Philadelphia 76ers',
'Phoenix Suns',
'Portland Trail Blazers',
'Sacramento Kings',
'San Antonio Spurs',
'Toronto Raptors',
'Utah Jazz',
'Washington Wizards']
team_names = numpy.array(team_list)
team_name_dropdown_options = [{'label': i, 'value': i} for i in team_names]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(style={'backgroundColor':'blue'}),
    html.Img(src=app.get_asset_url('img.png'),style={'display':'block','margin-left': 'auto', 'margin-right': 'auto'}),
    html.H2("Home Team"),
    dcc.Dropdown(
        id='home_team',
        options=team_name_dropdown_options,
        value=''
    ),
    html.H2("Away Team"),
    dcc.Dropdown(
        id='away_team',
        options=team_name_dropdown_options,
        value=''
    ),
    html.H3(id='output_text')
])


@app.callback(
    Output('output_text', 'children'),
    Input('home_team', 'value'),
    Input('away_team', 'value'),
)
def update_output_div(home_team, away_team):
    response = requests.get(
        'http://127.0.0.1:8000/predict_nba_home_team_win/',
        params={'team_home': home_team,
                'team_away': away_team},
    )
    json_response = response.json()
    winning_team = home_team if json_response['result'] == 1 else away_team
    probability_of_winning = json_response['win_probability'] if winning_team \
                                                                == home_team \
        else 1 - json_response['win_probability']
    if home_team == '' or away_team == '':
        return ''
    elif home_team == away_team:
        return f'Please select 2 different Teams'
    else:
        return f'{winning_team} will win with a probability of ' \
            f'{round(probability_of_winning * 100)}%'


if __name__ == '__main__':
    app.run_server(debug=True)