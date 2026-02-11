import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

T = int(input())
for tc in range(1,T+1):
    k = int(input())
    mg1 = deque(list(map(int,input().split())))
    mg2 = deque(list(map(int,input().split())))
    mg3 = deque(list(map(int,input().split())))
    mg4 = deque(list(map(int,input().split())))

    magnets = [mg1,mg2,mg3,mg4]

    # 화살표: 0 , 우측 접점: 2, 좌측 접점: 6

    for _ in range(k):
        # 돌아갈 자석 번호: 1, 2, 3, 4
        # 시계방향: 1 / 반시계방향: -1
        mg_num, dr = map(int,input().split())

        magnets = [mg1, mg2, mg3, mg4]

        # 현재 연결된 데이터 확인 : 0
        contact = [0,0,0,0]
        cont = 0
        for i,mg in enumerate(magnets[:3]):
            if mg[2] != magnets[i+1][6]:
                contact[i+1] = cont
            else:
                cont += 1
                contact[i + 1] = cont
        #print(contact)

        # 자석 번호가 홀수일때, 짝수 번호는 반대로 돈다
        if mg_num % 2:
            roll_data = [dr,-dr,dr,-dr]
        # 자석 번호가 짝수일때
        else:
            roll_data = [-dr,dr,-dr,dr]

        # contact 데이터를 보며, 해당 index와 값이 같은것만 돌아가게 하기
        target = contact[mg_num-1]

        for idx,c in enumerate(contact):
            # 돌릴 톱니와 연결되어 있는지 확인
            if c != target:
                continue
            # 연결되어 있다면 인덱스로 접근해서 돌리기
            # 시계방향 돌리기 => pop해서 append left
            # 반시계방향 돌리기 => popleft 해서 append
            # 시계방향인 경우
            if roll_data[idx] > 0:
                magnets[idx].appendleft(magnets[idx].pop())
            # 반시계방향인 경우
            else:
                magnets[idx].append(magnets[idx].popleft())

    score = 0

    # 다 돌고 난 뒤에 인덱스 0에 있는 값 받아오기
    # n극: 0 / S극: 1
    for idx,magnet in enumerate(magnets):
        if magnet[0] == 1:
            score += 2**idx

    print(f"#{tc} {score}")




