class Sport:
    # These variable initializations is what was causing
    # the error with basketball teams being added to all
    # of the Sports.
    # ball_type = ""
    # name = ""
    # equipment = []
    # teams = []

    #constructor function
    def __init__(self, ball_type, name, equipment):
        self.ball_type = ball_type 
        self.name = name 
        self.equipment = equipment
        # Added this in to replace the class-level initialization
        self.teams = []

    #setter function
    def addTeam (self, team):
        self.teams.append(team)

    #function
    def listTeams (self):
        # iterate through the teams list and print each one
        for team in self.teams:
            print(team)

    # getter function
    def getTeams (self):
        return self.teams
