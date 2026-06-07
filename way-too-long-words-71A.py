import sys;

input = sys.stdin.readline
def changeLongWordsToAbbrev(word):
    N = len(word)-1;
    abbrev = "";
    if N > 10:
        abbrev = word[0]+str(N-2)+word[N-1];
        return abbrev
    return word;


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        word = input();
        print(changeLongWordsToAbbrev(word))