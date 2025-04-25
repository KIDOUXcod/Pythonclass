class Player:
    def __init__(self, name, position):
        self.playerName = name
        self.playerPosition = position

    def __str__(self):
        return f"{self.playerName} ({self.playerPosition})"

class NFLTeam:
    def __init__(self, team_name, players):
        self.teamName = team_name
        self.players = players

    def display_team(self): 
        print(f"\nTeam: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f"- {player}")

# Create players
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Create the players list
playerList = [player1, player2, player3, player4]

# Create team
team = NFLTeam("San Francisco 49ers", playerList)

# Display team info
team.display_team()