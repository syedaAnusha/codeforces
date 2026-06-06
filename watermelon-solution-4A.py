import sys

# Fast I/O setup
input = sys.stdin.readline

def checkWeighForWatermelon():
        w = int(input());
        if w >= 1 and w <= 100:
            if w > 2 and not w & 1 :
                return "YES";
            return "NO"
        return -1;

if __name__ == "__main__":
    print(checkWeighForWatermelon());