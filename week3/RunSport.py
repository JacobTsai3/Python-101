from Sport import Sport
from Team import Team
import csv

debug = False

# Sport(ball_type, name, equipment)
basketball = Sport("basketball", "Basketball", ["hoop", "backboard", "court", "shoes"])
baseball = Sport("baseball", "Baseball", ["bat", "mound", "bases", "mit", "cleats"])
tennis = Sport("tennis", "Tennis", ["racket", "tennis_shoes", "net", "tennis_court"])
soccer = Sport("soccer", "Soccer", ["soccer_cleats", "goal", "field", "shin_guards", "high_socks"])
football = Sport("football", "Football", ["football_cleats", "field_goal", "field", "pads", "helmet"])

# sport_data_file: 'basketball.csv' aka the file name
# sport_data: the 'basketball.csv' file opened (aka the data within the file)
# sport_reader: pointer into the 'basketball.csv' file that can access the actual data
# row: the data on the line that sport_reader is pointing to

def readData(sport_data_file):
    with open(sport_data_file, newline='') as sport_data:
        sport_reader = csv.reader(sport_data)
        teams_data = []
        for row in sport_reader:
            # row: ['basketball', 'Brooklyn', '0', 'Nets', 'Kevin', 'Kyrie', 'Ben']
            teams_data.append(row)

    return teams_data

def setupSport(teams_data, sport):
    teams = []
    if(debug):
        print("Debug Statements:")
        print("teams_data: ")
        print(teams_data)

    for team_data in teams_data:
        # Team parameters: players, sport, city, rank, name
        players = []
        index = 4

        # team_data = [basketball,Brooklyn,0,Nets,Kevin,Kyrie,Ben]
        # len(team_data) = 7
        # index = 4
        # is index < len(team_data) --> is 4 < 7 --> TRUE
            # team_data[index] == index[4] == "Kevin"
            # players.append("Kevin")
            # index = index + 1 --> index = 4 + 1 --> index = 5

        # is index < len(team_data) --> is 5 < 7 --> TRUE
            # team_data[index] == index[5] == "Kyrie"
            # players.append("Kyrie")
            # index = index + 1 --> index = 5 + 1 --> index = 6

        # is index < len(team_data) --> is 6 < 7 --> TRUE
            # team_data[index] == index[5] == "Ben"
            # players.append("Ben")
            # index = index + 1 --> index = 6 + 1 --> index = 7
        
        # is index < len(team_data) --> is 7 < 7 --> FALSE
        if(debug):
            print("team_data: ")
            print(team_data)
        
        while(index < len(team_data)):
            players.append(team_data[index])
            index = index + 1

        if(debug):
            print("players:")
            print(players)
            print("team_data[0]:")
            print(team_data[0])
            print("team_data[1]:")
            print(team_data[1])
            print("team_data[2]:")
            print(team_data[2])
            print("team_data[3]:")
            print(team_data[3])
            print("End Debug Statements")

        new_team = Team(players, team_data[0], team_data[1], int(team_data[2]), team_data[3])
        teams.append(new_team)

    for team_object in teams:
        if(debug):
            print("Adding the " + team_object.getName() + " to " + team_object.getSport())
        sport.addTeam(team_object)

    sport.listTeams()

basketball_teams_data = readData('basketball.csv')
baseball_teams_data = readData('baseball.csv')
soccer_teams_data = readData('soccer.csv')
tennis_teams_data = readData('tennis.csv')
football_teams_data = readData('football.csv')

setupSport(basketball_teams_data, basketball)
setupSport(baseball_teams_data, baseball)
setupSport(soccer_teams_data, soccer)
setupSport(tennis_teams_data, tennis)
setupSport(football_teams_data, football)