T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))

    count = 0
    for w in range(N):
        word = 0
        for h in range(N):
            if puzzle[w][h] == 0:
                if word == K:
                    count += 1
                word = 0
            else:
                word += 1
        if word == K:
            count += 1

    for h in range(N):
        word = 0
        for w in range(N):
            if puzzle[w][h] == 0:
                if word == K:
                    count += 1
                word = 0
            else:
                word += 1
        if word == K:
            count += 1
        
    print("#%d %d" % (tc, count))