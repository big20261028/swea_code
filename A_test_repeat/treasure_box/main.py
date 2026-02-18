import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    codes = list(input())

    # deque로 바꾸기
    queue = deque(codes)

    # 4로 나누기
    code_len = N//4

    code_list = set()

    # 비밀번호 길이만큼 돌리기
    for r in range(code_len):
        last_char = queue.pop()
        queue.appendleft(last_char)

        # 4등분 해서 코드 목록에 넣기
        for n in range(1,5):
            start_index = (n*code_len) - code_len
            end_index = n * code_len
            target = list(queue)[start_index:end_index]
            target = ''.join(target)
            code_list.add(target)

    #print(code_list)
    # 숫자로 변환
    code_list = list(code_list)
    for i in range(len(code_list)):
        code_list[i] = int(code_list[i],16)
    #print(code_list)
    # 정렬
    code_list.sort(reverse=True)
    # 인덱스 K-1 위치 값 출력
    print(f'#{tc} {code_list[K-1]}')

