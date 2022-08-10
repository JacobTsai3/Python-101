from Sport import Sport
from Team import Team

# Sport(ball_type, name, equipment)
basketball = Sport("basketball", "Basketball", ["hoop", "backboard", "court", "shoes"])
baseball = Sport("baseball", "Baseball", ["bat", "mound", "bases", "mit", "cleats"])
tennis = Sport("tennis", "Tennis", ["racket", "tennis_shoes", "net", "tennis_court"])
soccer = Sport("soccer", "Soccer", ["soccer_cleats", "goal", "field", "shin_guards", "high_socks"])
football = Sport("football", "Football", ["football_cleats", "field_goal", "field", "pads", "helmet"])

basketball_teams_data = [ 
                        [ ["Kevin", "Kyrie", "Ben"], "basketball", "Brooklyn", 0, "Nets"],
                        [ ["Quentin", "Julius", "Jalen"], "basketball", "NY", 0, "Knicks"],
                        [ ["LeBron", "Russell", "Anthony"], "basketball", "Los Angeles", 0, "Lakers"],
                        [ ["Jalen", "Jabari", "Kevin"], "basketball", "Houston", 0, "Rockets"],
                        [ ["Luka", "Boban", "Spencer"], "basketball", "Dallas", 0, "Mavericks"],
                        [ ["Paolo", "Bol", "Mohamed"], "basketball", "Orlando", 0, "Magic"]
                    ]

baseball_teams_data = [ 
                            [ ["Fernando", "Jurickson", "Juan"], "baseball", "San Diego", 0, "Padres"],
                            [ ["Mookie", "Freddie", "Clayton"], "baseball", "Los Angeles", 0, "Dodgers"],
                            [ ["Randy", "Brandon", "Yandy"], "baseball", "Tampa Bay", 0, "Rays"],
                            [ ["Jorge", "Cedric", "Roughned"], "baseball", "Baltimore", 0, "Orioles"],
                            [ ["Ronald", "Dansby", "Kenley"], "baseball", "Atlanta", 0, "Braves"],
                            [ ["Aaron", "Gerrit", "Aroldis"], "baseball", "NY", 0, "Yankees"]
                        ]

soccer_teams_data = [ 
                            [ ["Son", "Harry", "Pierre"], "soccer", "Tottenham", 0, "Hotspurs"],
                            [ ["Kylian", "Lionel", "Neymar"], "soccer", "Paris Saint-Germain", 0, "FC"],
                            [ ["Mohammed", "Virgil", "Joel"], "soccer", "Liverpool", 0, "FC"],
                            [ ["Alphonso", "Sadio", "Noussair"], "soccer", "Bayern Munich", 0, "FC"],
                            [ ["Bruno", "Christiano", "Marcus"], "soccer", "Manchester United", 0, "FC"],
                            [ ["Erling", "Kevin", "Ilkay"], "soccer", "Manchester City", 0, "FC"]
                        ]

football_teams_data = [ 
                            [ ["Dak", "Ceedee", "Ezekial"], "football", "Dallas", 0, "Cowboys"],
                            [ ["Justin", "Austin", "Keenan"], "football", "Los Angeles", 0, "Chargers"],
                            [ ["Derek", "Davante", "Josh"], "football", "Las Vegas", 0, "Raiders"],
                            [ ["Joe", "Ja'Maar", "Eli"], "football", "Cincinnati", 0, "Bengals"],
                            [ ["Russell", "Jerry", "Bradley"], "football", "Denver", 0, "Broncos"],
                            [ ["D.K.", "Tyler", "Rashaad"], "football", "Seattle", 0, "Seahawks"]
                        ]

tennis_teams_data = [ 
                            [ ["Duckworth", "Kygrios", "Minaur"], "tennis", "Australia", 0, "Team"],
                            [ ["Medvedev", "Rublev", "Khachanov"], "tennis", "Russia", 0, "Team"],
                            [ ["Fritz", "Opelka", "Tiafoe"], "tennis", "USA", 0, "Team"],
                            [ ["Nadal", "Alcaraz", "Bautista"], "tennis", "Spain", 0, "Team"],
                            [ ["Zverev", "Otte", "Altmaier"], "tennis", "Germany", 0, "Team"],
                            [ ["Djokovic", "Kecmanovic", "Krajinovic"], "tennis", "Serbia", 0, "Team"]
                        ]

def setupSport(teams_data, sport):
    teams = []

    for team_data in teams_data:
        new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
        teams.append(new_team)

    for team_object in teams:
        print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        sport.addTeam(team_object)

    sport.listTeams()

setupSport(basketball_teams_data, basketball)
setupSport(baseball_teams_data, baseball)
setupSport(soccer_teams_data, soccer)
setupSport(tennis_teams_data, tennis)
setupSport(football_teams_data, football)