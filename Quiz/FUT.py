

PLAYERS = {
    'Karim Benzema': 93, # player's name: his rating
    'Robert Lewandowski': 94,
    'Kylian Mbappe': 97,
    'Luka Modric': 90,
    'Pedri': 93,
    'Pique': 88,
}

LEGENDARIES = {
    'Lionel Messi': (98, 1.1), # legendary player's name: (his rating, his chemistry booster value)
    'Cristiano Ronaldo': (97, 1.05),
}

class Team:
    """FIFA Ultimate Team"""
    def __init__(self,name,squad=None):
        """assign attributes to team"""
        if len(squad==0):
            rating=0
            squad=[]
        for i in squad:
            if i in PLAYERS:
                sum_rating=PLAYERS[i]
        rating=sum_rating/len(squad)
        self.squad=squad
        self.rating=rating
        self.name=name
        
    def __str__(self):
        """Return a string representation of this team, including team name and squad."""
        if len(self.squad)==0:
            l=f"{self.name} has no players yet"
        else:
            l=f"{self.name} has {self.squad}"
            for i in self.squad:
                self.squad=','.join
        return l

    def choose(self, player):
        """choose one player from PLAYERS and update team's rating which is the average rating of entire current squad.

        player: string
        """
        if player in PLAYERS:
            self.squad+=player
        for i in self.squad:
            if i in PLAYERS:
                sum_rating=self.rating+PLAYERS[i]
        rating=sum_rating/len(self.squad)
        self.rating=rating
        return self.squad

    def choose_legendary(self, player):
        """choose one player from LEGENDARIES and update team's rating which is the average rating of entire current squad multiplied by legendary's booster.

        player: string
        """
        if player in PLAYERS:
            self.squad+=player
        for i in self.squad:
            if i in PLAYERS:
                sum_rating=self.rating+PLAYERS[i]
                multiplier=PLAYERS[i][1]
            rating=(sum_rating/len(self.squad))*[multiplier]
            self.rating=rating
        return self.squad
    def __gt__(self,team):


#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team('Real Madrid', initial_players=['Karim Benzema'])
    barcelona = Team('Barcelona')
    print('Before choosing squad:')
    print(real_madrid)
    print(barcelona)
    print()
    print('After choosing squad:')
    real_madrid.choose('Luka Modric')
    real_madrid.choose('Kylian Mbappe')
    barcelona.choose('Pique')
    barcelona.choose('Pedri')
    barcelona.choose('Robert Lewandowski')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)
    print()
    print('After choosing legendary:')
    real_madrid.choose_legendary('Cristiano Ronaldo')
    barcelona.choose_legendary('Lionel Messi')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)


if __name__ == '__main__':
    main()