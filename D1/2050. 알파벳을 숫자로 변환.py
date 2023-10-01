T = input()
arr = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, char in enumerate(T):
    idx = arr.index(char)
    if i == len(T) - 1:  # 마지막 요소인 경우
        print(idx, end="")
    else:
        print(idx, end=" ")