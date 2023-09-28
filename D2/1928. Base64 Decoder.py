from  base64 import b64decode

T = int(input())

for test_case in range(1, T + 1):
    text = input()
    res = b64decode(text).decode('UTF-8')

    print("#%d %s" %(test_case, res))

'''
0. 이게 왜 D1...? 문제 이해가 너무 어려웠다.
TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u

1. 문제 이해
    - 1byte = 8bit
    - 24bit 버퍼 안에 한 byte씩 세 byte = 3 글자 (1byte = 1 글자)
    - 6bit = 000000(0)~111111(63)
    - input 4글자 = output 3글자

2. 풀이 순서
    i.   4 글자씩: 문자를 인덱스값으로 변환
    ii.  인덱스값을 2진수로 변환
    iii. 6비트를 채우기 위해 0으로 채움
    iv.  6비트씩 1 글자를 만듦

3. zfill()
    - 자릿수만큼 0으로 채우는 함수

4. base64 라이브러리
    - b64decode(): Base64 문자열을 이진 데이터로 디코딩
    - decode('UTF-8): 이진 데이터를 문자열로 변환
'''