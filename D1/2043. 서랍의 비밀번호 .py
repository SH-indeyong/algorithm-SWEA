l = list(map(int, input().split()))
p = l[0]
k = l[1]
n = 0

for i in range(k, p+1):
    n += 1
print(n)