'''
가위 1
바위 2
보 3
'''

l = list(map(int, input().split()))
a = l[0]
b = l[1]
if ((a == 1 and b == 3) or a > b):
    print("A")
else:
    print("B")