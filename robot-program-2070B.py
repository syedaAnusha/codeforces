import sys;

input = sys.stdin.readline
def countNumberOfTimesRobotEnterAtPointZero(command, n, x, k):
    i = 0;
    time = 1;
    cnt = 0;
    while i < n and time <= k:
        if command[i] == "L":
            x = x - 1;
        else:
            x = x + 1;
        if x == 0 and time <= k:
            cnt += 1; 
            i = -1;
        time += 1;
        i += 1;
    return cnt;
    
if __name__ == "__main__":
    noOfTestCases = int(input());
    for _ in range(noOfTestCases):
        n, x, k  = map(int, input().split());
        command = input();
        print(countNumberOfTimesRobotEnterAtPointZero(command, n, x, k));