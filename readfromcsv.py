# This module reads from the csv, and stores the data into a dataframe

import pandas as pd

def readplayers(): 

    # Reads from csv
    headers = ['Name','Score']
    players = pd.read_csv("playerlist.csv", names=headers)
    players.set_index('Name')    
    
    # Returns from dataframe
    return players

if __name__ == '__main__':
    readplayers()