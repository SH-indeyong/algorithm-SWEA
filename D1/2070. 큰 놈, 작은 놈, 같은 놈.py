T = int(input())
res = ''

for test_case in range(1, T+1):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    if (a < b):
        res = '<'
    elif (a > b):
        res = '>'
    else:
        res = '='
    print("#%d %s" % (test_case, res))