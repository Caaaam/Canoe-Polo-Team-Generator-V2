# This is our main file

import readfromcsv 
import playerclass
import teammakerclass

# Returns players dataframe from readfromcsv module
players = readfromcsv.readplayers()

#define playerlist to contain class instances of players
playerlist = []

for row, val in players.iterrows():
    playerlist.append(playerclass.player(players['Name'][row],players['Score'][row]))
    # Uncomment below to see players/score
    #playerclass.player.showplayer(playerlist[row])


# Calls teammakerclass to sort into even teams
Teams = teammakerclass.TeamMaker(playerlist)

# Prints teams to screen, in future, update this output
print('\nWelcome to the Team Generator V2')

teammakerclass.TeamMaker.getteams(Teams)

print(f'\nThis attempts the algorithm {teammakerclass.TeamMaker.getiterations(Teams)} times and returns the best result.\n')