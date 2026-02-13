import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    words = list(input().split())
    #print(words)

    middle = N//2
    if N%2 : middle += 1

    front = words[:middle]
    back = words[middle:]

    #print(front)
    #print(back)

    result = []

    for i in range(middle):
        if len(front) > i:
            result.append(front[i])
        if len(back) > i :
            result.append(back[i])
    result = " ".join(result)
    print(f'#{tc} {result}')
