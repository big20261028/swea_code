import sys

sys.stdin = open('sample_input.txt','r')

'''
가장 빨리 내려갈 수 있는 시간 구하기

[제약 사항]

1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 3초

2. 방의 한 변의 길이 N은 4 이상 10 이하의 정수이다. (4 ≤ N ≤ 10)

3. 사람의 수는 1 이상 10 이하의 정수이다. (1 ≤ 사람의 수 ≤ 10)

4. 계단의 입구는 반드시 2개이며, 서로 위치가 겹치지 않는다.

5. 계단의 길이는 2 이상 10 이하의 정수이다. (2 ≤ 계단의 길이 ≤ 10)

6. 초기에 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 서로 겹치지 않는다.
'''

# 사람이 있는 좌표값 리스트 만들기
def get_positions(matrix):
    p_pos_list = []
    s_pos_list = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                p_pos_list.append((i,j))
            elif matrix[i][j] > 1:
                s_pos_list.append((i,j))
    return p_pos_list,s_pos_list

# 부분집합 구하기
def subset_tools(deps,visited):
    if deps == people_cnt:
        temp_list = [[],[]]
        for i in range(people_cnt):
            if visited[i]:
                temp_list[0].append(p_pos_list[i])
            else:
                temp_list[1].append(p_pos_list[i])
        subset_list.append(temp_list)
        return

    visited[deps] = True
    subset_tools(deps+1,visited)

    visited[deps] = False
    subset_tools(deps+1,visited)

# 해당 계단으로 들어간 사람들이 다 내려가는데 걸리는 시간 return
def cal_down_time(peoples,stair):
    if len(peoples) < 1:
        return 0

    stair_time_a = []
    for xa, ya in peoples:
        xat, yat = stair
        require_time = abs(xa - xat) + abs(ya - yat)
        stair_time_a.append(require_time)
    # 먼저 도착한 순서대로 정렬
    stair_time_a.sort()
    # 기다릴 시간 추가
    for i in range(len(stair_time_a)):
        if i <= 2:
            stair_time_a[i] += matrix[stair[0]][stair[1]] + 1
            continue
        need_time = max(stair_time_a[i - 3],stair_time_a[i]+1)
        stair_time_a[i] += need_time + matrix[stair[0]][stair[1]]
    return stair_time_a.pop()

# 부분집합을 돌며 최솟값 갱신
def find_min_time(subset_list):
    global min_time

    # 1번 계단으로 들어갈 사람 그룹 / 2번 계단으로 들어갈 사람들
    for groupA,groupB in subset_list:
        time_a = cal_down_time(groupA,s_pos_list[0])
        time_b = cal_down_time(groupB,s_pos_list[1])
        total_t = max(time_a,time_b)
        min_time = min(min_time,total_t)

        time_a = cal_down_time(groupA, s_pos_list[1])
        time_b = cal_down_time(groupB, s_pos_list[0])
        total_t = max(time_a, time_b)
        min_time = min(min_time, total_t)

# 각 계단마다 사람들 도착 시간 순서대로 줄새워서 리스트 만들기
# 도착한 사람의 좌표를 리스트에서 popleft 시키고 set 데이터에 넣기
# while문 돌다가 set 데이터가 사람의 수와 같아지면 break
T = int(input())
#T = 4
for tc in range(1,T+1):
    # 방 한 변의 길이
    N = int(input())
    # 사람 : 1 / 계단 : 2 이상
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 사람의 수 구하기
    people_cnt = 0
    for row in matrix:
        people_cnt += row.count(1)

    # 사람,계단의 좌표 구하기
    p_pos_list,s_pos_list = get_positions(matrix)

    # 가장 짧은 시간
    min_time = float('inf')

    # 사람이 1명인 경우
    # 각 계단 좌표로 이동하는데 걸리는 시간 + 내려가는 시간 중 가장 작은 값이 정답
    if len(p_pos_list) == 1:
        for x,y in s_pos_list:
            i,j = p_pos_list[0]
            stair = abs(i-x) + abs(j-y) + 1 + matrix[x][y]
            min_time = min(min_time,stair)
        print(f'#{tc} {min_time}')
        continue

    # 부분집합 구하기
    visited = [False] * people_cnt
    #
    subset_list = []
    subset_tools(0, visited)

    #print(list(com_list))

    # for item in subset_list:
    #     print(item)
    # print('-'*40)

    find_min_time(subset_list)

    print(f'#{tc} {min_time}')

