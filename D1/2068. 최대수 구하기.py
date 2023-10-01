T = int(input())

for test_case in range(1, T+1):
    l = list(map(int, input().split()))
    m = max(l)
    print("#%d %d" % (test_case, m))
