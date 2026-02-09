### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

n / 4 만큼 돌릴 수 있다.
돌리면 초기값으로 돌아오니 n/4가 3이라면 그냥 3회 돌려라
인덱스로 객체 3개씩 잘라서 리스트에 넣어라. 이미 리스트에 있으면 넣지마라

배열에서 한번 돌릴때마다 맨 뒤에 있던게 맨 앞으로 온다.
'''
from collections import deque

# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    arr = list(input())

    queue = deque(arr)

    length = n//4

    num_list = []
    for r in range(length):
        back = queue.pop()
        queue.appendleft(back)

        for i in range(0,n,length):
            data = list(queue)[i:i+length]
            data = ''.join(data)
            if data not in num_list:
                num_list.append(data)

    #print(num_list)

    num_list = list(map(lambda x : int(x,16), num_list))

    num_list.sort(reverse=True)
    #print(num_list)


    result = num_list[k-1]
    print(f"#{test_case} {result}")
