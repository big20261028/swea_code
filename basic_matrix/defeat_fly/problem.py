### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

시작지점부터 m만큼 이중 for문 돌면서 value 더하기
'''
def kill_fly(pos,size,mat_data):
    # pos = (i,j) 데이터
    # size = m 파리채 크기
    # mat_data = 검색할 데이터 리스트
    kill_cnt = 0
    for i in range(pos[0], (pos[0] + size)):
        if not (0 <= i < n):
            break
        for j in range(pos[1], (pos[1] + size)):
            if not (0 <= j < n):
                break
            kill_cnt += mat_data[i][j]
            #print(kill_cnt)
    return kill_cnt

# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n) ]

    max_cnt = 0
    for i in range(n):
        for j in range(n):
            kill_cnt = kill_fly((i,j),m,arr)
            if kill_cnt > max_cnt:
                max_cnt = kill_cnt

    result = max_cnt
    print(f"#{test_case} {result}")
