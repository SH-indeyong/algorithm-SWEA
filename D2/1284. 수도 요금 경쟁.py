'''
WL 사용
A사: (P * W)원
B사: 
    if (W > R): Q + ((W-R) * S)원
    else: Q원
P, Q, R, S, W
'''

T = int(input())

for tc in range(1, T+1):
    l = list(map(int, input().split()))
    P = l[0]
    Q = l[1]
    R = l[2]
    S = l[3]
    W = l[4]

    wonA = P * W
    if (W > R):
        wonB = Q + ((W-R)*S)
    else:
        wonB = Q
    
    if wonA < wonB:
        res = wonA
    else:
        res = wonB
    print("#%d %d" % (tc, res))