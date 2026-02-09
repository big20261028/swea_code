### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

좌표 기준 8방향으로 본인과 같은 색깔을 처음 만날때까지 이동
같은 색깔을 만나면 여태 지나왔던 좌표의 색깔을 변환
 
'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    orders = [ list(map(int, input().split())) for _ in range(m) ]
    table = [ list(0 for _ in range(n)) for _ in range(n) ]

    # 0:빈칸  1: 흑돌 2: 백돌
    # 시작 세팅 2x2
    st = (n//2) - 1
    table[st][st] = 2
    table[st+1][st] = 1
    table[st][st+1] = 1
    table[st+1][st+1] = 2
    # print(n,m)
    # print(orders)
    # print(table)
    # 서, 서북, 북, 북동, 동, 동남, 남, 남서
    dxy = [ (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1) ]

    for x, y, c in orders:
        x -= 1
        y -= 1
        table[x][y] = c
        for dx,dy in dxy:
            temp_list = []
            nx = x + dx
            ny = y + dy
            while True:
                if not (0 <= nx < n and 0 <= ny < n):
                    temp_list.clear()
                    break
                # 빈칸인 경우
                if table[nx][ny] == 0:
                    temp_list.clear()
                    break
                # 시작지점과 같은 색인 경우
                elif table[nx][ny] == c:
                    break
                # 다음 지점이 판 밖을 나가버리지 않을때만
                else:
                    temp_list.append((nx,ny))
                nx += dx
                ny += dy
            #print(temp_list)
            if len(temp_list) != 0:
                for tx, ty in temp_list:
                    table[tx][ty] = c
        # for item in table:
        #     print(item)
        # print("-"*30)

    w_cnt = [ item.count(2) for item in table ]
    w_cnt = sum(w_cnt)
    b_cnt = [ item.count(1) for item in table ]
    b_cnt = sum(b_cnt)

    result = None
    print(f"#{test_case} {b_cnt} {w_cnt}")
