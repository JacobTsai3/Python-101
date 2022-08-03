from Sport import Sport
from Team import Team

# Sport(ball_type, name, equipment)
basketball = Sport("basketball", "Basketball", ["hoop", "backboard", "court", "shoes"])
baseball = Sport("baseball", "Baseball", ["bat", "mound", "bases", "mit", "cleats"])
tennis = Sport("tennis", "Tennis", ["racket", "tennis_shoes", "net", "tennis_court"])
soccer = Sport("soccer", "Soccer", ["soccer_cleats", "goal", "field", "shin_guards", "high_socks"])
football = Sport("football", "Football", ["football_cleats", "field_goal", "field", "pads", "helmet"])

def setupBasketball():
    # Team(players, sport, city, rank, name)
    basketball_teams_data = [ 
                            [ ["Kevin", "Kyrie", "Ben"], "basketball", "Brooklyn", 0, "Nets"],
                            [ ["Quentin", "Julius", "Jalen"], "basketball", "NY", 0, "Knicks"],
                            [ ["LeBron", "Russell", "Anthony"], "basketball", "Los Angeles", 0, "Lakers"],
                            [ ["Jalen", "Jabari", "Kevin"], "basketball", "Houston", 0, "Rockets"],
                            [ ["Luka", "Boban", "Spencer"], "basketball", "Dallas", 0, "Mavericks"],
                            [ ["Paolo", "Bol", "Mohamed"], "basketball", "Orlando", 0, "Magic"]
                        ]

    basketball_teams = []

    # Team(players, sport, city, rank, name)
    for team_data in basketball_teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        basketball_teams.append(new_team)

    for team_object in basketball_teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        basketball.addTeam(team_object)

    basketball.listTeams()

def setupBaseball():
    print("TODO")

def setupTennis():
    print("TODO")

def setupSoccer():
    print("TODO")

def setupFootball():
    print("TODO")

setupBasketball()
setupBaseball()
setupTennis()
setupSoccer()
setupFootball()