matches = [
    {
        'home_team': 'Liverpool',
        'away_team': 'Manchester City',
        'home_score': 4,
        'away_score': 3,
        'winner': 'Liverpool'
    },
    {
        'home_team': 'Manchester United',
        'away_team': 'Tottenham',
        'home_score': 1,
        'away_score': 0,
        'winner': 'Manchester United'
    },
    {
        'home_team': 'Chelsea',
        'away_team': 'Arsenal',
        'home_score': 2,
        'away_score': 2,
        'winner': 'Draw'
    }
]

print(matches)

matches_with_winner = filter(lambda match: match['winner'] != 'Draw', matches)
#print(list(matches_with_winner))
new_matches_with_winner = []
new_matches_with_winner = list(map(lambda match: 'Winner: ' + match['home_team'], matches_with_winner))
print(new_matches_with_winner)