import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_does_not_find_player(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_finds_players(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_does_not_find_players(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )