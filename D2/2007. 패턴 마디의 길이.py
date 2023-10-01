T = int(input())

for tc in range(T, T+1):
    text = input()
    t = text[0]
    pattern = []
    next_pattern = []
    word = []
    
    for i in range(11):
        pattern = text[:i]
        next_pattern = text[i:i*2]
        if (pattern == next_pattern):
            word = pattern
        
    print("#%d %d" % (tc, len(word)))