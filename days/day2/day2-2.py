from typing import List
from util import getLines, printAnswer

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


def minCubes(rounds):
    output = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for round in rounds:
        for color, count in round.items():
            if (count > output[color]):
                output[color] = count

    return output


def getPower(games):
    totalSumPowers = 0
    for _, rounds in games.items():
        output = minCubes(rounds)
        power = output['green'] * output['red'] * output['blue']
        totalSumPowers += power

    return totalSumPowers


def main():
    lines = getLines("day2.txt")
    games = parseGames(lines)

    answer = getPower(games)
    
    printAnswer(answer)


main()
