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
    baseball_teams_data = [ 
                            [ ["Fernando", "Jurickson", "Juan"], "baseball", "San Diego", 0, "Padres"],
                            [ ["Mookie", "Freddie", "Clayton"], "baseball", "Los Angeles", 0, "Dodgers"],
                            [ ["Randy", "Brandon", "Yandy"], "baseball", "Tampa Bay", 0, "Rays"],
                            [ ["Jorge", "Cedric", "Roughned"], "baseball", "Baltimore", 0, "Orioles"],
                            [ ["Ronald", "Dansby", "Kenley"], "baseball", "Atlanta", 0, "Braves"],
                            [ ["Aaron", "Gerrit", "Aroldis"], "baseball", "NY", 0, "Yankees"]
                        ]

    baseball_teams = []

    for team_data in baseball_teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        baseball_teams.append(new_team)

    for team_object in baseball_teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        baseball.addTeam(team_object)

    baseball.listTeams()
    

def setupTennis():
    tennis_teams_data = [ 
                            [ ["Duckworth", "Kygrios", "Minaur"], "tennis", "Team", 0, "Australia"],
                            [ ["Medvedev", "Rublev", "Khachanov"], "tennis", "Team", 0, "Russia"],
                            [ ["Fritz", "Opelka", "Tiafoe"], "tennis", "Team", 0, "USA"],
                            [ ["Nadal", "Alcaraz", "Bautista"], "tennis", "Team", 0, "Spain"],
                            [ ["Zverev", "Otte", "Altmaier"], "tennis", "Team", 0, "Germany"],
                            [ ["Djokovic", "Kecmanovic", "Krajinovic"], "tennis", "Team", 0, "Serbia"]
                        ]

    tennis_teams = []

    for team_data in tennis_teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        tennis_teams.append(new_team)

    for team_object in tennis_teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        tennis.addTeam(team_object)

    tennis.listTeams()
    

def setupSoccer():
    soccer_teams_data = [ 
                            [ ["Son", "Harry", "Pierre"], "soccer", "Tottenham", 0, "Hotspurs"],
                            [ ["Kylian", "Lionel", "Neymar"], "soccer", "Paris", 0, "Saint-Germain"],
                            [ ["Mohammed", "Virgil", "Joel"], "soccer", "Liverpool", 0, "FC"],
                            [ ["Alphonso", "Sadio", "Noussair"], "soccer", "Bayern Munich", 0, "FC"],
                            [ ["Bruno", "Christiano", "Marcus"], "soccer", "Manchester United", 0, "FC"],
                            [ ["Erling", "Kevin", "Ilkay"], "soccer", "Manchester City", 0, "FC"]
                        ]

    soccer_teams = []

    for team_data in soccer_teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        soccer_teams.append(new_team)

    for team_object in soccer_teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        soccer.addTeam(team_object)

    soccer.listTeams()
    

def setupFootball():
    football_teams_data = [ 
                            [ ["Dak", "Ceedee", "Ezekial"], "football", "Dallas", 0, "Cowboys"],
                            [ ["Justin", "Austin", "Keenan"], "football", "Los Angeles", 0, "Chargers"],
                            [ ["Derek", "Davante", "Josh"], "football", "Las Vegas", 0, "Raiders"],
                            [ ["Joe", "Ja'Maar", "Eli"], "football", "Cincinnati", 0, "Bengals"],
                            [ ["Russell", "Jerry", "Bradley"], "football", "Denver", 0, "Broncos"],
                            [ ["D.K.", "Tyler", "Rashaad"], "football", "Seattle", 0, "Seahawks"]
                        ]

    football_teams = []

    for team_data in football_teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        football_teams.append(new_team)

    for team_object in football_teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        football.addTeam(team_object)

    football.listTeams()
    

setupBasketball()
setupBaseball()
setupTennis()
setupSoccer()
setupFootball()