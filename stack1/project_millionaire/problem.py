### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
#T = 2
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    #print(arr)

    stack = []
    # 최댓값인 날에 이전 날짜 물품을 다 판다.
    # 최댓값인 날 이후부터의 최댓값인 날을 찾는다 (반복)
    # 최댓값과 값이 같은 경우 break

    # 맨 뒤에서부터 시작
    # 시작지점보다 작은 데이터들 쭉 더하기
    # 큰 값 나오면 모두 더하고 시작지점 갱신
    target = arr[::-1]
    max_price = target[0]
    benefit = 0
    for item in target:
        #print(item,max_price)
        if item <= max_price:
            benefit += max_price - item
        elif item > max_price:
            max_price = item




    #print(money)
    result = benefit
    print(f"#{test_case} {result}")
