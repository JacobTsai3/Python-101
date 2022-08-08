from Sport import Sport
from Team import Team

basketball_teams_data = [ 
                            [ ["Kevin", "Kyrie", "Ben"], "basketball", "Brooklyn", 0, "Nets"],
                            [ ["Quentin", "Julius", "Jalen"], "basketball", "NY", 0, "Knicks"],
                            [ ["LeBron", "Russell", "Anthony"], "basketball", "Los Angeles", 0, "Lakers"],
                            [ ["Jalen", "Jabari", "Kevin"], "basketball", "Houston", 0, "Rockets"],
                            [ ["Luka", "Boban", "Spencer"], "basketball", "Dallas", 0, "Mavericks"],
                            [ ["Paolo", "Bol", "Mohamed"], "basketball", "Orlando", 0, "Magic"]
                        ]

basketball_teams = []

# for team_data in basketball_teams_data:
#         new_team = Team(team_data[0], team_data[1], team_data[2], team_data[3], team_data[4])
#         basketball_teams.append(new_team)

# Without a for-loop:

# Save each team's data
team1_data = basketball_teams_data[0]
team2_data = basketball_teams_data[1]
team3_data = basketball_teams_data[2]
team4_data = basketball_teams_data[3]
team5_data = basketball_teams_data[4]
team6_data = basketball_teams_data[5]

# Print each team's data
print("Team 1 data:")
print(team1_data)
print("Team 2 data:")
print(team2_data)
print("Team 3 data:")
print(team3_data)
print("Team 4 data:")
print(team4_data)
print("Team 5 data:")
print(team5_data)
print("Team 6 data:")
print(team6_data)

# Create each team object
team1 = Team(team1_data[0], team1_data[1], team1_data[2], team1_data[3], team1_data[4])
team2 = Team(team2_data[0], team2_data[1], team2_data[2], team2_data[3], team2_data[4])
team3 = Team(team3_data[0], team3_data[1], team3_data[2], team3_data[3], team3_data[4])
team4 = Team(team4_data[0], team4_data[1], team4_data[2], team4_data[3], team4_data[4])
team5 = Team(team5_data[0], team5_data[1], team5_data[2], team5_data[3], team5_data[4])
team6 = Team(team6_data[0], team6_data[1], team6_data[2], team6_data[3], team6_data[4])

print("Team 1 object:")
print(team1)
print("Team 2 object:")
print(team2)
print("Team 3 object:")
print(team3)
print("Team 4 object:")
print(team4)
print("Team 5 object:")
print(team5)
print("Team 6 object:")
print(team6)