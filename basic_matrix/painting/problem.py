### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
from pprint import pprint
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    paint_data = [ list(map(int, input().split())) for _ in range(N) ]

    paint_map = [ list(0 for _ in range(10)) for _ in range(10) ]

    for item in paint_data:
        start_r, start_c, end_r, end_c, color = item
        for i in range(start_r,end_r+1):
            for j in range(start_c,end_c+1):
                if color == 1:
                    if paint_map[i][j] == 0:
                        paint_map[i][j] = color
                    elif paint_map[i][j] == 2:
                        paint_map[i][j] = 3
                elif color == 2:
                    if paint_map[i][j] == 0:
                        paint_map[i][j] = color
                    elif paint_map[i][j] == 1:
                        paint_map[i][j] = 3


    #pprint(paint_map)
    total = 0
    for item in paint_map:
        total += item.count(3)

    result = total
    print(f"#{test_case} {result}")
