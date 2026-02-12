import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    words = [list(input()) for _ in range(5) ]

    result = ''
    for i in range(15):
        for word in words:
            #print(word)
            if i < len(word):
                result += word[i]
                #print(result)

    print(f'#{tc} {result}')