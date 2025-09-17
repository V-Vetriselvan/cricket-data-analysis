# IPL Ball-by-Ball Quickstart (script version)
# Usage:
#   1) Place deliveries.csv and matches.csv next to this script
#   2) Run: python ipl_quickstart.py

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

DELIVERIES = 'deliveries.csv'
MATCHES = 'matches.csv'

missing = [p for p in [DELIVERIES, MATCHES] if not os.path.exists(p)]
if missing:
    print('Missing files:', missing)
    print('Please place deliveries.csv and matches.csv in the same folder and rerun.')
    sys.exit(1)

deliveries = pd.read_csv(DELIVERIES)
matches = pd.read_csv(MATCHES)

print('deliveries shape:', deliveries.shape)
print('matches shape   :', matches.shape)

# Top batsmen
batsman_runs = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print('\nTop 10 Run Scorers:')
print(batsman_runs)

plt.figure(figsize=(10,6))
batsman_runs.plot(kind='bar')
plt.title('Top 10 Run Scorers in IPL (dataset)')
plt.ylabel('Runs')
plt.xlabel('Batsman')
plt.tight_layout()
plt.savefig('top_batsmen.png')
print('Saved chart: top_batsmen.png')

# Wickets
wickets = deliveries[deliveries['dismissal_kind'].notna()]
bowler_wickets = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)
print('\nTop 10 Wicket Takers:')
print(bowler_wickets)

plt.figure(figsize=(10,6))
bowler_wickets.plot(kind='bar')
plt.title('Top 10 Wicket Takers (dataset)')
plt.ylabel('Wickets')
plt.xlabel('Bowler')
plt.tight_layout()
plt.savefig('top_bowlers.png')
print('Saved chart: top_bowlers.png')

# Team wins
team_wins = matches['winner'].value_counts().head(10)
print('\nMost Successful Teams (by wins):')
print(team_wins)

plt.figure(figsize=(10,6))
team_wins.plot(kind='bar')
plt.title('Most Successful Teams (by wins)')
plt.ylabel('Wins')
plt.xlabel('Team')
plt.tight_layout()
plt.savefig('team_wins.png')
print('Saved chart: team_wins.png')

# Save CSVs
batsman_runs.to_csv('top_batsmen.csv')
bowler_wickets.to_csv('top_bowlers.csv')
team_wins.to_csv('team_wins.csv')
print('Saved: top_batsmen.csv, top_bowlers.csv, team_wins.csv')
