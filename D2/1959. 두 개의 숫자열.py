T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    collect = []

    if N<M:
        big = M
        small = N
        bigList = B
        smallList = A
    else:
        big = N
        small = M
        bigList = A
        smallList = B

    for i in range(big-small+1):
        res = 0
        for j in range(small):
            res += smallList[j] * bigList[i+j]
        collect.append(res)

    print("#%d %d" % (tc, max(collect)))