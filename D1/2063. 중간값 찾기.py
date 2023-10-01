T = int(input())

l = list(map(int, input().split()))
l.sort()
mid = l[int(T/2)]
print("%d" % (mid))