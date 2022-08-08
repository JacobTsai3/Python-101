class Team:

    def __init__(self, players, sport, city, rank, name):
        self.players = players 
        self.sport = sport
        self.city = city
        self.rank = rank
        self.name = name

    def __str__(self):
        print_string = "The " + self.name
        print_string = print_string + " from " + self.city
        print_string = print_string + " is ranked " + str(self.rank)
        print_string = print_string + " in " + self.sport + ".\n"
        print_string = print_string + "Roster:\n"
        for player in self.players:
            print_string = print_string + player + "\n"
        return print_string

    def addPlayer (self, player):
        (self.players).append(player)  
    
    def listPlayers (self):
        print("players")

    def removePlayer (self, player):
        (self.players).remove(player)

    def getRank (self):
        return self.rank

    def getPlayers (self):
        return self.players

    def getCity (self):
        return self.city

    def updateCity (self, city):
        self.updateCity = city

    def updateRank (self, rank):
        self.updateRank = rank

    def getSport (self):
        return self.sport
    
    def getName (self):
        return self.name
    
    
