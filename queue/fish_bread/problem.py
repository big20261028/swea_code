### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

front 변수 선언 = -1

1 ≤ N, M, K ≤ 100
'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m,k = map(int,input().split())
    times = list(map(int, input().split()))

    times.sort()
    result = 'Possible'
    #print(times)
    sold = 0
    for t in times:
        stock = ((t//m) * k) - sold
        if stock <= 0:
            result = 'Impossible'
            break
        sold += 1
    #result = None
    print(f"#{test_case} {result}")
