### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_in.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

괴물의 위치부터 델타탐색으로 사방으로 퍼지며 1을 만날때까지 3으로 바꾸기
이후 0의 개수 cnt

'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n) ]

    # 괴물의 위치 찾기
    x,y = 0,0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                x,y = i,j

    dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]
    for dx,dy in dxy:
        nx,ny = x,y
        while True:
            nx += dx
            ny += dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] != 1:
                matrix[nx][ny] = 3
            else:
                break

    # 값이 0인 객체 개수 합산
    total = 0
    for row in matrix:
        total += row.count(0)

    result = total
    print(f"#{test_case} {result}")
