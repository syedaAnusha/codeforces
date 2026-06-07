import sys;

input = sys.stdin.readline
def getTotalNumberOfFizzBuzzCnt(num):
    cnt = 0;
    quo = num // 15;
    rem = num % 15;
    cnt = (quo * 3) + min(rem, 2) + 1;
    return cnt;

if __name__ == "__main__":
    noOfTestCases = int(input());
    for _ in range(noOfTestCases):
        num = int(input());
        print(getTotalNumberOfFizzBuzzCnt(num));