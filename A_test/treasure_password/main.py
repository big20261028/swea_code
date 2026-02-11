import sys
sys.stdin = open('sample_input.txt','r')


from collections import deque
T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    text = deque(list(input()))

    # 각 모서리의 숫자 갯수는 n//4 개씩 있다.
    # for문을 n//4번 돌린다.
    codes = set()

    for i in range(n//4):
        # 시계방향으로 돌리기
        text.appendleft(text.pop())
        # 돌린 값을 4등분해서 set에 add
        string = ''.join(text)
        for j in range(4):
            start = j * n//4
            end = start + n//4
            codes.add(string[start:end])

    codes = list(codes)

    #print(codes)
    result = []

    for item in codes:
        result.append(int(item,16))

    #print(result)
    result.sort(reverse=True)
    print(f'#{tc} {result[k-1]}')
