import sys;

input = sys.stdin.readline;

def getDistinctLettersCountFrom(username):
    unique_set = set(username);
    return len(unique_set)-1;



def findUsernameGender(s):
    if getDistinctLettersCountFrom(s) & 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")

if __name__ == "__main__":
    s = input();
    findUsernameGender(s);