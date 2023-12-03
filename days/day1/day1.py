from util import getLines

def findCode(line: str):
    nums = [char for char in line if str.isnumeric(char)]

    if(len(nums) == 1):
        return int(nums[0] + nums[0])
    else:
        return int(nums[0] + nums[-1])

def main():
    lines = getLines('day1.txt')
    output = []
    for line in lines:
        output.append(findCode(line))
    
    print(sum(output))
    
main()