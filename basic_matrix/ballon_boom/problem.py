### 제출 전에 지우기 ###
import sys
sys.stdin = open("input1.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

문제 이해 실패
재시도
풍선을 선택하면 풍선 value만큼 사방향으로 퍼지며 풍선을 터트린다
이때 터진 풍선들의 value들의 합 중에 최대값을 구하는 문제 
'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    result = 0
    for i in range(N):
        for j in range(M):
            target_val = matrix[i][j]
            max_num = target_val
            for n in range(4):
                ni = i
                nj = j
                for _ in range(target_val):
                    ni += dx[n]
                    nj += dy[n]

                    if 0 <= ni < N and 0 <= nj < M:
                        max_num += matrix[ni][nj]
                        # 타겟 풍선의 크기와 상관 없음
                        # if matrix[i][j] < matrix[ni][nj]:
                        #     max_num += matrix[i][j]
                        # elif matrix[i][j] >  matrix[ni][nj]:
                        #     max_num += matrix[ni][nj]
            #print(f"{i},{j} max_num = {max_num}")
            if max_num > result:
                result = max_num

    print(f"#{test_case} {result}")
