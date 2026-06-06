import sys;

input = sys.stdin.readline;

def findYears(a,b):
    years = 1;
    a = (a << 1) + a;
    b = (b << 1);
    while a <= b:
        years += 1;
        a = (a << 1) + a;
        b = (b << 1);
    return years;

if __name__ == "__main__":
    limakWeight, bobWeight = map(int, input().split());
    print(findYears(limakWeight, bobWeight));