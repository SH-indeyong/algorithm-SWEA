T = int(input())

for tc in range(1, T+1):
    last = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    l = list(map(int, input().split()))
    m1 = l[0]
    d1 = l[1]
    m2 = l[2]
    d2 = l[3]

    day = 0
    
    if (m1 == m2):
        day = d2 - d1 + 1
    else:
        day = d2 + (last[m1] - d1) + 1
        while(m2 - 1 > m1):
            m2 -= 1 
            day += last[m2]

    print("#%d %d" % (tc, day))