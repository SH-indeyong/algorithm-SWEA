import math

T = int(input())

for test_case in range(1, T+1):
    l = list(map(int, input().split()))
    hap = 0
    avg = 0.0
    for i in range(0, len(l)):
        hap += l[i]
    avg = round(hap/10, 0)
    print("#%d %d" % (test_case, avg))