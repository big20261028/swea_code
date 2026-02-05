### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    #N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(9) ]

    #print(matrix)

    # 가로세로 데이터 등록
    target_data = []
    for col in range(9):
        temp_list = []
        for row in range(9):
            temp_list.append(matrix[row][col])
        target_data.append(temp_list)
    target_data.extend(matrix)

    # 3*3 데이터 등록
    for row in range(0,9,3):
        for col in range(0,9,3):
            temp_list = []
            # 기준점에서 3*3 이동하며 등록
            for i in range(row,row+3):
                for j in range(col,col+3):
                    temp_list.append(matrix[i][j])
            target_data.append(temp_list)

    # print(len(target_data))
    # 모두 set에 넣었다가 빼기
    # len이 모두 9로 유지되어 있다면 print(1)
    # 아니라면 print(0)
    target_data = [ set(item) for item in target_data ]

    result = 1

    for item in target_data:
        if len(item) != 9:
            result = 0
            break

    print(f"#{test_case} {result}")
