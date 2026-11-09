import unittest

from src.player import Player, PlayerStats


class PlayerReaderStub:
    """Tarjoaa testien tarvitsemat pelaajat ilman verkkoyhteyttä."""

    def __init__(self):
        self.players = [
            Player({
                "name": "Dallas One",
                "nationality": "FIN",
                "assists": 10,
                "goals": 5,
                "team": "DAL",
                "games": 20,
                "id": 1
            }),
            Player({
                "name": "Dallas Two",
                "nationality": "SWE",
                "assists": 15,
                "goals": 8,
                "team": "DAL",
                "games": 20,
                "id": 2
            }),
            Player({
                "name": "Other Team",
                "nationality": "FIN",
                "assists": 30,
                "goals": 20,
                "team": "TOR",
                "games": 20,
                "id": 3
            })
        ]

    def get_player(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Other Team", "Dallas One"]
        )

    def test_top_scorers_by_nationality_returns_empty_list_for_unknown_nationality(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(players, [])

    def test_top_scorers_by_team_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(
            [player.name for player in players],
            ["Dallas Two", "Dallas One"]
        )

    def test_top_goal_scorers_returns_requested_number_of_players(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Other Team", "Dallas Two"]
        )


if __name__ == "__main__":
    unittest.main()
