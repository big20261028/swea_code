import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,num = input().split()
    N = int(N)

    binary = [0] * (len(num) * 4)

    int_val = int(num,16)
    i = len(binary)
    while int_val:
        i -= 1
        if int_val%2:
            binary[i] = 1
        int_val //= 2
    binary = ''.join(map(str,binary))
    print(f'#{tc} {binary}')