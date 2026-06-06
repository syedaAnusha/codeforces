import sys;

input = sys.stdin.readline;

def findSteps(x):
    steps = 0;
    quotient = x // 5;
    remainder = x % 5;
    steps += quotient;
    if remainder != 0:
        steps += 1;
    return steps;

if __name__ == "__main__":
    inp = int(input());
    print(findSteps(inp));