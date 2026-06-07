import sys;

input = sys.stdin.readline
def team(problems):
    totalSum = sum(problems);
    problemCnt = 0;
    if totalSum > 1:
        problemCnt += 1;
    return problemCnt;

if __name__ == "__main__":
    numOfQuestions = int(input()); 
    numOfQuestionsImplement = 0;
    for _ in range(numOfQuestions):
        problems = list(map(int, input().split()));
        numOfQuestionsImplement += team(problems);
    print(numOfQuestionsImplement);