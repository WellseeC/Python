'''
This program is experienced for repeated code
'''

def hh(country):
    points = num_wins * 3+num_draw
    goal_adv = goals_for - goals_against
    print(country)
    print("Win:", num_wins, "Lose:", num_losses, "Draw:", num_draw)
    print("Total number of points:", points, "Goal advantage:", goal_adv)
## Process results for Germany
num_wins = 2
num_losses = 1 
num_draw = 0
goals_for = 7
goals_against = 2
country=hh('Germany')
## Process results for USA
num_wins = 1
num_draw = 1
num_losses = 1 
goals_for = 4
goals_against = 4
country=hh('USA')
## Process results for Argentina
num_wins = 3
num_draw = 0
num_losses = 0 
goals_for = 6
goals_against = 3
country=hh('Argentina')
## Process results for England
num_wins = 0
num_draw = 1
num_losses = 2 
goals_for = 2
goals_against = 4
country=hh('England')