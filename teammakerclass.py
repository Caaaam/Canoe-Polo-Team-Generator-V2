class TeamMaker:

    def __init__(self, playerlist):
        self.playerlist = playerlist

        # Define number of teams  
        if len(self.playerlist) > 19:
            numteams = 4 
        elif len(self.playerlist) > 14:
            numteams = 3
        else:
            numteams = 2 

        # Initialising a dictionary for teams 
        self.teams = {}

        # Assigning the n highest players to each team
        for n in range(numteams): 
            Teamname = "Team " + str(n+1)
            self.teams.update({Teamname : self.playerlist[n].getname()})

        # NOTETOSELF: INSERT SOME ALGORITHM TO SORT THE REMAINING PLAYERS #

    def getteams(self):
        return self.teams

if __name__ == '__main__':
   TeamMaker()
   TeamMaker().getteams()