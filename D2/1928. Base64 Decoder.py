char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']

T = int(input())

for test_case in range(1, T + 1):
    text = list(input())
    s = ''
    res = ''
    
    for i in range(len(text)):
        idx_to_bin = 0
        idx_to_bin = bin(char.index(text[i]))[2:]
        length = len(idx_to_bin)
        
        while (len(idx_to_bin) < 6):
            idx_to_bin = '0' + idx_to_bin
    # print(idx_to_bin)
        s = s + idx_to_bin

    for j in range(0, len(s), 8):
        res += chr(int(s[j:j+8], 2))

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
'''