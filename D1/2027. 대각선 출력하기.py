a = '+++++'
a = list(a)


for j in range(0, 5):
    a[j] = '#'
    print(''.join(a))
    a[j] = '+'