from typing import List
from util import getLines


def getRounds(roundsStr: str) -> List:
    rounds = roundsStr.split(";")
    output = []
    for round in rounds:
        input = round.strip().split(", ")
        curr = {}
        for hand in input:
            count, color = hand.split(" ")
            curr[color] = int(count)
        output.append(curr)
    return output


def parseGames(lines: List[str]):
    games = {}
    for line in lines:
        game, roundsStr = line.split(":")
        id = game.split(" ")[1]
        rounds = getRounds(roundsStr)
        games[id] = rounds
    return games


def checkGame(rounds):
    for round in rounds:
        print(round)
        if (('red' in round and round['red'] > 12)
                or ('green' in round and round['green'] > 13)
                or ('blue' in round and round['blue'] > 14)
            ):
            return False
    return True


def checkGames(games: dict):
    ids = []

    for id, rounds in games.items():
        if (checkGame(rounds)):
            ids.append(int(id))

    return ids


def main():
    lines = getLines("day2.txt")
    games = parseGames(lines)
    gameIds = checkGames(games)

    print(gameIds)
    print(sum(gameIds))


main()
