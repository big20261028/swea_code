import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 벽돌을 부수는 함수
def break_bricks(pos,matrix):

    queue = deque()












T = int(input())

for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(H) ]

    # 관리하기 편하도록 2차원 리스트를 시계방향으로 회전
    matrix2 = zip(*matrix)

    # for row in matrix:
    #     print(row)


    max_val = 0


