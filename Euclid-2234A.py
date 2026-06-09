import sys;

input = sys.stdin.readline
def findPair(nums, k):
    nums.sort();
    nums = nums[::-1];
    b = [0]*k;
    b[0] = nums[0];
    b[1] = nums[1];
    i = 0;
    while i < k-2:
        # edge case, [0, 0, 0, 0]
        if b[i+1] == 0:
            break;
        b[i+2] = b[i] % b[i+1];
        i += 1;
    
    if nums == b:
        print(nums[0], nums[1]);
    else:
        print(-1);
    return;

if __name__ == "__main__":
    noOfTestCases = int(input());
    for _ in range(noOfTestCases):
        k = int(input());
        nums = list(map(int, input().split()));
        findPair(nums, k);