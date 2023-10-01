T = int(input())
m_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T+1):
    n = input()
    y = n[:4]
    m = n[4:6]
    d = n[6:]
    if (int(m) < 1 or int(m) > 12 or int(d) > m_day[int(m)-1]):
        print("#%d -1" % (test_case))
    else:
        print("#%d %s/%s/%s" % (test_case, y, m, d))

'''
month의 day 정보를 리스트로 넣어두고 비교하기
'''