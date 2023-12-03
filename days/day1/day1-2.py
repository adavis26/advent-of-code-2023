import sys
sys.path.append('../') 

from util import getLines, printAnswer

numMap = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def getCleanLine(line: str) -> str:
    i = 0
    p = 1
    while i < len(line):
        if line[i:p] in numMap:
            line = line[:i] + numMap[line[i:p]] + line[p+1:]
            i = p + 1
        else:
            if p >= len(line):
                i += 1
                p = 1
            else:
                p += 1

    return line


def findCode(line: str):
    cleanLine = getCleanLine(line)

    nums = [char for char in cleanLine if str.isnumeric(char)]

    if (len(nums) == 1):
        return int(nums[0] + nums[0])
    else:
        return int(nums[0] + nums[-1])


def main():
    lines = getLines('day1.txt')
    output = []
    for line in lines:
        code = findCode(line)
        output.append(code)

    answer = sum(output)
    printAnswer(answer)

main()
