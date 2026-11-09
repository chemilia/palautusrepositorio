from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    console = Console()

    table = Table(title="NHL Players")

    table.add_column("Name", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", style="green", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )

    console.print(table)

if __name__ == "__main__":
    main()
