T = int(input())

for tc in range(1, T+1):
    text = input()
    pattern = []
    next_pattern = []
    l=0
    
    for i in range(11):
        pattern = text[:i]
        next_pattern = text[i:i*2]
        if (i != 0 and pattern == next_pattern):
            l = len(pattern)
            break

    print("#%d %d" % (tc, l))

    '''
    i=0 인 경우 pattern == next_pattern 만족하므로 예외처리
    '''