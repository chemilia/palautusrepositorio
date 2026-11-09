"""Kokeilu NHL-pelaajien tilastojen käsittelyllä."""
from player import PlayerReader
from player import PlayerStats

URL = "https://studies.cs.helsinki.fi/nhlstats/2026-27/players"
stats = PlayerStats(PlayerReader(URL))

for p in stats.top_scorers_by_team("DAL"):
    print(p)
