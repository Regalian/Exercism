from collections import defaultdict
from enum import Enum
from dataclasses import dataclass


class ResultType(Enum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"


@dataclass
class Result:
    team: str
    result: ResultType


@dataclass
class TeamStats:
    matches: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0
    points: int = 0


POINTS: dict[ResultType, int] = {
    ResultType.WIN: 3,
    ResultType.DRAW: 1,
    ResultType.LOSS: 0,
}


class ColumnWidths(Enum):
    TEAM = 30
    MATCHES = 2
    WINS = 2
    DRAWS = 2
    LOSSES = 2
    POINTS = 2


class ErrorMessages(Enum):
    INVALID_RESULT = "Invalid result: {}"


def parse_match(match: str) -> tuple[Result, Result]:
    """
    Parse a match string into two Result objects.

    Args:
        match (str): The match string in the format "home;away;result".

    Returns:
        tuple[Result, Result]: A tuple containing the home and away Result objects.
    """
    home, away, result = (x.strip() for x in match.split(";"))
    if result == ResultType.WIN.value:
        return Result(home, ResultType.WIN), Result(away, ResultType.LOSS)
    elif result == ResultType.LOSS.value:
        return Result(home, ResultType.LOSS), Result(away, ResultType.WIN)
    elif result == ResultType.DRAW.value:
        return Result(home, ResultType.DRAW), Result(away, ResultType.DRAW)
    else:
        raise ValueError(ErrorMessages.INVALID_RESULT.value.format(result))


def update_results(season: dict[str, TeamStats], home: Result, away: Result) -> None:
    """Update team statistics based on match results.

    Args:
        season (dict[str, TeamStats]): The season dictionary containing team statistics.
        home (Result): The result of the home team.
        away (Result): The result of the away team.
    """
    season[home.team].matches += 1
    season[away.team].matches += 1
    season[home.team].wins += 1 if home.result == ResultType.WIN else 0
    season[away.team].wins += 1 if away.result == ResultType.WIN else 0
    season[home.team].draws += 1 if home.result == ResultType.DRAW else 0
    season[away.team].draws += 1 if away.result == ResultType.DRAW else 0
    season[home.team].losses += 1 if home.result == ResultType.LOSS else 0
    season[away.team].losses += 1 if away.result == ResultType.LOSS else 0
    season[home.team].points += POINTS[home.result]
    season[away.team].points += POINTS[away.result]


def construct_table(season: dict[str, TeamStats]) -> list[str]:
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted(season.items(), key=lambda x: (-x[1].points, x[0])):
        table.append(
            f"{team.ljust(ColumnWidths.TEAM.value)} | {stats.matches:{ColumnWidths.MATCHES.value}} | {stats.wins:{ColumnWidths.WINS.value}} | {stats.draws:{ColumnWidths.DRAWS.value}} | {stats.losses:{ColumnWidths.LOSSES.value}} | {stats.points:{ColumnWidths.POINTS.value}}"
        )
    return table


def tally(rows: list[str]) -> list[str]:
    """Generate a league table from a list of matches.

    3 points for a win, 1 for a draw, 0 for a loss. Table is ordered by points. Tied teams are ordered alphabetically.

    Args:
        rows (list[str]): A list of match results in the format "Team1;Team2;Result".
    Returns:
        list[str]: A list of strings representing the league table.
    """
    season: defaultdict[str, TeamStats] = defaultdict(TeamStats)
    for row in rows:
        home, away = parse_match(row)
        update_results(season, home, away)

    return construct_table(season)
