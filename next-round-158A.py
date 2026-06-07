import sys;

input = sys.stdin.readline
def nextRound(scores, k):
    N = len(scores);
    cntOfQualifiedParticipants = 0;
    for i in range(N):
        if scores[i] > 0 and scores[i] >= scores[k-1]:
            cntOfQualifiedParticipants += 1;
        else:
            break;
    return cntOfQualifiedParticipants;


if __name__ == "__main__":
    n, k = map(int, input().split()); 
    scores = list(map(int, input().split()));
    print(nextRound(scores, k));