T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
      hap = 0
      num = input()
      data = list(map(int,num.split()))
      for i in range(len(data)):
            if data[i]%2 == 1:
                  hap += data[i]
      print('#%d %d' % (test_case, hap))