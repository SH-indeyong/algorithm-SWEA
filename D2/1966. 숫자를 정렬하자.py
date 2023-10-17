T = int(input())

for tc in range(1, T+1):
    length = int(input())
    # sorted(리스트명): 원래 리스트는 그대로
    # 리스트명.sort(): 원래 리스트 자체를 정렬
    new = sorted(list(map(int, input().split())))
    print("#%d %s" % (tc, format(' '.join(map(str, new)))))