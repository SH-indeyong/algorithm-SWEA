T = int(input())

for tc in range(1, T+1):
    text = input()
    l = len(text)
    i = 0
    res = 1

    for i in range(l):
        if (text[i] != text[l-i-1]):
            res = 0
    print("#%d %d" % (tc, res))