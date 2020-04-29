# Stores the player class, which contains player info

class player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def showplayer(self): 
        print(f"{self.name} has a score of {self.score}")

    def getname(self):
        return self.name

    def getscore(self):
        return self.score

#if __name__ == '__main__':
#    player()
#    player().showplayer()
#    player().getname()
#    player().getscore()