### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

연속된 숫자의 개수를 구하는 로직


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(n) ]

    line_list = []
    for item in matrix:
        line_list.append(item)
    for col in range(n):
        line_list.append([ matrix[row][col] for row in range(n)])

    #단어 퍼즐을 가로, 세로로 나눈 리스트 생성
    #print(line_list)
    result = 0
    for line in line_list:
        text = ''.join(map(str,line))
        text_list = text.split('0')
        for item in text_list:
            if len(item) == k:
                result += 1



    print(f"#{test_case} {result}")
