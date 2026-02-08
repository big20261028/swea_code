### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    containers = list(map(int,input().split()))
    trucks = list(map(int,input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    # print(containers)
    # print(trucks)

    used_trucks = []
    moved_container = []
    for w in containers:
        for t in trucks:
            if w <= t:
                #print(w,t)
                #used_trucks.append(t)
                trucks.remove(t)
                moved_container.append(w)
                break
    result = sum(moved_container)
    print(f"#{test_case} {result}")
