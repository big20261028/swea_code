import sys
sys.stdin = open('Sample_input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    trees = list(map(int,input().split()))

    max_h = max(trees)
    # 가장 큰 나무와의 차이 구하기
    total_diff = 0
    # 1만큼 키가 모자란 날 갯수 모아두기
    odd = 0

    for tree in trees:
        diff = max_h - tree
        total_diff += diff
        # if diff%2:
        #     odd += 1

    days = (total_diff//3)*2 + total_diff%3
    one_waters = days//2 + days%2
    two_waters = days//2

