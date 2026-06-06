import sys;

input = sys.stdin.readline
def removeSmallest(numsArr):
    N = len(numsArr)
    i = 0

    while i < N-1:
        if abs(numsArr[i+1]-numsArr[i]) > 1:
            return "NO"
        i += 1

    return "YES";

if __name__ == "__main__":
    noOfTestCases = int(input())
    for _ in range(noOfTestCases):
        a = int(input())
        numsArr = list(map(int, input().split()))
        numsArr.sort()
        print(removeSmallest(numsArr))