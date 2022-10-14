import json

with open('sportssofa_scores.json') as fp:
    json_data = json.load(fp)
    
league_str = json_data['events'][0]['tournament']['name']
hometeam_str = json_data['events'][0]['homeTeam']['name']
awayteam_str = json_data['events'][0]['awayTeam']['name']

homescore_str = json_data['events'][0]['homeScore']['current']
awayscore_str = json_data['events'][0]['awayScore']['current']

print(league_str, "|", hometeam_str, homescore_str, " - ", awayteam_str, awayscore_str)

for game in json_data['events']:
    league_str = game['tournament']['name']
    hometeam_str = game['homeTeam']['name']
    awayteam_str = game['awayTeam']['name']

    homescore_str = game['homeScore']['current']
    awayscore_str = game['awayScore']['current']
    
    print(league_str, "|", hometeam_str, homescore_str, " - ", awayteam_str, awayscore_str)