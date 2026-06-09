import sys;

input = sys.stdin.readline

def isPalindrom(num):
    numStr = str(num);
    if numStr == numStr[::-1]:
        return True;
    return False;

def findTerms(n):
    if n == 10:
        print(-1);
        return;

    rem = n % 12;
    if rem != 10 and isPalindrom(rem):
        b = n - rem;
        print(rem, b);
        return;
    elif rem == 10:
        a = 12 + rem;
        b = n - a;
        print(a, b);
        return;

if __name__ == "__main__":
    noOfTestCases = int(input());
    for _ in range(noOfTestCases):
        n = int(input());
        findTerms(n);