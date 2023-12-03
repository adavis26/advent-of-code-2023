def getLines(filename: str):
    with open(filename) as file:
        return [line.strip("\n") for line in file.readlines()]


def printAnswer(answer: str) -> None:
    print(f"\n{ '✏️ ' * 20 }\n\nAnswer: {answer}\n")
