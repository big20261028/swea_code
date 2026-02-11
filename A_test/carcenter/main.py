import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N,M,K,A,B = map(int,input().split())
    a1 = list(map(int,input().split()))
    b1 = list(map(int,input().split()))
    t1 = list(map(int,input().split()))


