### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
### 제출 전에 지우기 ###
'''
생각 정리용 공간
도착지점이 2로 되어있음!!!!
'''
#
def find_path(i,matrix):
    temp_matrix = [ list(0 for _ in range(100)) for _ in range(100)]

    # 오른쪽, 왼쪽, 아래 순서
    dxy = [ (0,1), (0,-1), (1,0) ]
    # matrix[0][i]가 출발점
    x, y =  0, i
    #print(f'시작 좌표 : {x},{y}')
    # 출발점을 왔던 지역 정보에 등록
    temp_matrix[x][y] = 1
    # 맵의 맨 밑에 도달하면 종료
    while x!=99:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 맵을 벗어 났는지 검사
            if 0 > nx or nx>= 100 or 0 > ny or ny >= 100:
                continue
            # temp_matrix의 좌표 값이 0인지 검사( 갔던곳인지 검사 )
            if temp_matrix[nx][ny] == 1:
                continue
            # matrix 상에 길이 있는지 검사
            if matrix[nx][ny] == 0:
                continue
            x,y = nx, ny
            temp_matrix[x][y] = 1
            break

    return matrix[x][y] == 2




# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(100) ]

    #검증
    # for item in matrix:
    #     print(item)

    result = None

    #시작지점 찾기
    for i in range(100):
        if matrix[0][i] == 1:
            if find_path(i,matrix):
                result = i
                break

    print(f"#{test_case} {result}")
