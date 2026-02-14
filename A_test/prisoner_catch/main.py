import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    # 세로크기, 가로크기, 맨홀 세로위치, 맨홀 가로위치, 탈출 소요시간
    N,M,R,C,L = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
