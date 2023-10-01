T = int(input())

for test_case in range(1, T+1):
    l = list(map(int, input().split()))
    q = l[0]/l[1]
    r = l[0]%l[1]
    print("#%d %d %d" % (test_case, q, r))