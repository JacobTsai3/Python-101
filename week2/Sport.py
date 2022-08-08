class Sport:

    #constructor function
    def __init__(self, ball_type, name, equipment):
        self.ball_type = ball_type 
        self.name = name 
        self.equipment = equipment
        self.teams = []

    #setter function
    def addTeam (self, team):
        (self.teams).append(team)

    #function
    def listTeams (self):
        # iterate through the teams list and print each one
        for team in self.teams:
            print(team)

    # getter function
    def getTeams (self):
        return self.teams
