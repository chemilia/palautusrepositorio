import requests

class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.id = player_dict['id']

    def __str__(self):
        return f"{self.name:20} {self.team:15}  {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_player(self):
        response = requests.get(self.url).json()
        
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_player()

        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)

        return sorted(nationality_players, key=lambda player:player.goals+player.assists, reverse=True)
