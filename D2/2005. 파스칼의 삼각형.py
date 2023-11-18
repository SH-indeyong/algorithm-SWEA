#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print("#%d" % (test_case))
    for i in range(1, N+1):
        l = []
        for j in range(i):
            if j == 0 or j == i-1:
                l.append(1)
            else:
                l.append(prev[j-1] + prev[j])
        prev = l
        print(' '.join(map(str, l)))