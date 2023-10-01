'''
N=2a x 3b x 5c x 7d x 11e
'''

T = int(input())
num = [2, 3, 5, 7, 11]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = [0, 0, 0, 0, 0]
    N = int(input())

    for i in range(len(num)):
        while (N%num[i] == 0):
            if N%num[i] == 0:
                N /= num[i]
                count[i] += 1

    print("#%d %d %d %d %d %d " % (test_case, count[0], count[1], count[2], count[3], count[4]))