def hh(country,num_wins,num_losses,num_draw,goals_for,goals_against):
    points = num_wins * 3+num_draw
    goal_adv = goals_for - goals_against
    print(country)
    print("Win:", num_wins, "Lose:", num_losses, "Draw:", num_draw)
    print("Total number of points:", points, "Goal advantage:", goal_adv)
    return hh
country = hh('Germany',2,1,0,7,2)
country = hh('USA',1,1,1,4,4)
country = hh('Argentina',3,0,0,6,3)
country = hh('England',0,1,2,2,4)
