T = int(input())

for test_case in range(1, T + 1):
    N = int(input())            # N마리 세기
    check = set()               # 이미 본 숫자를 저장하는 집합

    i = 0
    while len(check) < 10:
        i += 1
        # number마리의 양을 셈
        number = N * i
        # number를 숫자 하나씩 분리해서 check에 추가
        while number > 0:
            digit = number % 10
            print(digit)
            check.add(digit)
            number //= 10

    print("#%d %d" % (test_case, N * i))