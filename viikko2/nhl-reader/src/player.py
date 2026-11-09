"""Sisältää NHL-pelaajien tiedot, lukemisen ja tilastojen käsittelyn."""
import requests

class Player:
    """Kuvaa yksittäistä NHL-pelaajaa ja hänen tilastojaan."""
    def __init__(self, player_dict):
        """Alustaa pelaajan tiedot sanakirjasta."""

        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.id = player_dict['id']

    def __str__(self):
        """Palauttaa pelaajan tiedot merkkijonona."""

        return f"{self.name:20} {self.team:15}  {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    """Hakee NHL-pelaajien tiedot verkkopalvelusta."""

    def __init__(self, url):
        """Alustaa pelaajatietojen lähdeosoitteen."""

        self.url = url

    def get_player(self):
        """Hakee pelaajat verkkopalvelusta ja palauttaa pelaajaoliot."""

        response = requests.get(self.url, timeout = 10).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    """Käsittelee NHL-pelaajien tilastoja."""

    def __init__(self, reader):
        """Alustaa tilastojen käsittelyyn käytettävän lukijan."""

        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        """Palauttaa kansallisuuden mukaiset pelaajat pistejärjestyksessä."""

        players = self.reader.get_player()

        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)

        return sorted(nationality_players, key=lambda player:player.goals+player.assists, reverse=True)

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pistejärjestyksessä."""
        players = self.reader.get_player()

        team_players = [
            player for player in players
            if player.team == team
        ]

        return sorted(
            team_players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = self.reader.get_player()

        return sorted(
            players,
            key=lambda player: player.goals,
            reverse=True
        )[:how_many]
