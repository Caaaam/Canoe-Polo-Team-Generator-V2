import random 
import statistics

class TeamMaker:

    def __init__(self, playerlist):
        self.playerlist = playerlist

        self.numofteams()
        self.sortteams()

    def numofteams(self): 
        # Define number of teams  
        if len(self.playerlist) > 19:
            self.numteams = 4 
        elif len(self.playerlist) > 14:
            self.numteams = 3
        else:
            self.numteams = 2  
        #print(f"\nThere are {self.numteams} teams.")      

    def sortteams(self):
        # Define a number of 'bins' to sort players in to
        self.numbins = int(len(self.playerlist)/self.numteams) + len(self.playerlist)%self.numteams
        
        # Defining the set up for each team in the following loop
        self.teamsetup = {} 
        self.teamsetupscores = {}
        self.teamsetupstdev = {}

        # Number of iterations to try 
        self.iterations = 500

        for i in range(self.iterations):

            # Initialising a dictionary for bins
            self.bins = {}

            # Assigning n players to each bin 
            start = 0 
            for n in range(self.numbins): 
                Binname = "Bin " + str(n+1)
                for m in range(start, start + self.numteams):
                    try: 
                        self.bins.setdefault(Binname, []).append(self.playerlist[m])       
                    except IndexError:
                        break
                # Randomises the list in each bin    
                random.shuffle(self.bins[Binname])
                # Sets the start point for each bin to be 
                start += len(self.bins['Bin 1'])
            #print(self.bins)

            # Initialising a dictionary for teams 
            self.teams = {}
            self.scores = {} 

            # Assigning the n highest players to each team
            start = 0 
            for n in range(self.numteams): 
                Teamname = "Team " + str(n+1)
                for m in range(start, start + self.numbins):
                    # To cancel out the increasing index
                    binnamer = m - start
                    Binname = "Bin " + str(binnamer+1)

                    # Try statement to deal with different numbers on each team
                    try: 
                        self.teams.setdefault(Teamname, []).append(self.bins[Binname][n].getname())
                        self.scores.setdefault(Teamname, []).append(self.bins[Binname][n].getscore())
                    except IndexError: 
                        break
                start += len(self.teams['Team 1'])
        
            # Saving each set up 
            Teamsetupname = "Team Set " + str(i+1)
            self.teamsetup.setdefault(Teamsetupname, []).append(self.teams)
            # Appending stdev of average scores to
            StDevList = [] 
            for index in self.teams:
                self.teamsetupscores.setdefault(Teamsetupname, []).append(sum(self.scores[index])/len(self.teams[index]))
                StDevList.append(sum(self.scores[index])/len(self.teams[index]))
            StDev = statistics.stdev(StDevList)    
            self.teamsetupstdev.setdefault(Teamsetupname, []).append(StDev)
            

        # Gets the key corrisponding the the teamset with the lowest stdev
        bestteams = min(self.teamsetupstdev, key = self.teamsetupstdev.get)
        self.teams = self.teamsetup[bestteams][0]
        self.scores = self.teamsetupscores[bestteams]
        
    def getteams(self):
        counter = 0
        for index in self.teams:
            print(f"{index} : {self.teams[index]} with an average player score of: {round(self.scores[counter],2)}")
            counter += 1     

    def getiterations(self):
        return self.iterations       

#if __name__ == '__main__':
#   Maker = TeamMaker(playerlist)
#   Maker.getteams()
#   Maker.sortteams()
#   Maker.numofteams()