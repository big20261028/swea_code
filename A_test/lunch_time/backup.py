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
from collections import deque

# 사람이 있는 좌표값 리스트 만들기
def get_people_positions(matrix):
    pos_list = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                pos_list.append((i,j))
    return pos_list

# 각 계단마다 사람들 도착 시간 순서대로 줄새워서 리스트 만들기
# 도착한 사람의 좌표를 리스트에서 popleft 시키고 set 데이터에 넣기
# while문 돌다가 set 데이터가 사람의 수와 같아지면 break
T = int(input())
for tc in range(1,T+1):
    # 방 한 변의 길이
    N = int(input())
    # 사람 : 1 / 계단 : 2 이상
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 사람의 수 구하기
    people_cnt = 0
    for row in matrix:
        people_cnt += row.count(1)

    # 사람의 좌표 구하기
    pos_list = get_people_positions(matrix)

    # 각 계단별 사람 좌표 리스트 순회
    # 도달까지 걸리는 시간 기준으로 정렬
    # deque로 변형 및 추가 소요 시간 가공
    # 첫 3칸까지는 도달까지 걸리는 시간 + 계단내려가는 시간
    # 3칸 앞에 있는 객체 시간 + 도달까지 걸리는 시간 + 계단 내려가는 시간
    # 가공 후 리스트에 일괄 보관
    deque_list = []
    for i in range(N):
        for j in range(N):
            # 2보다 작으면 continue
            if matrix[i][j] < 2: continue
            # 리스트 생성
            temp_list = []
            # 사람 좌표 순회, 도달 시간 정보 등록
            for x,y in pos_list:
                require_time = abs(x-i) + abs(y-j)
                temp_dict = [ (x,y),require_time ]
                temp_list.append(temp_dict)
            # 도달 시간 기준으로 정렬
            temp_list.sort(key=lambda x : x[1])
            # 정렬된 리스트 순회하며 기다릴 시간 추가
            for n in range(len(temp_list)):
                (x,y),t = temp_list[n]
                if n <= 2:
                    # 처음 계단에 들어온 3인은 바로 계단 내려감
                    temp_list[n] = [(x,y), t + matrix[i][j] + 1]
                    continue
                # 나중 계단에 들어온 사람은 자신보다 3만큼 먼저 들어온 사람이 나갈때까지 기다림
                temp_list[n] = [(x, y), t + matrix[i][j] + temp_list[n-3][1] + 1]

            # 최종적으로 완성된 리스트를 deque로 변환 후 deque_list에 append
            temp_deque = deque(temp_list)
            deque_list.append(temp_deque)

    #print(len(deque_list))

    # 시간을 돌리며 각 queue 첫번째를 꺼내 시간과 일치하는지 검사. 일치하면 pass_pos에 추가
    pass_pos = set()
    t = 0
    while len(pass_pos) < people_cnt:
        t += 1
        for queue in deque_list:
            while queue:
                target = queue.popleft()
                (x, y), require_t = target
                # 시간과 일치하지 않는 경우 다시 queue 넣고 break
                if require_t != t:
                    queue.appendleft(target)
                    break
                # 일치하는 경우 pass_pos에 추가
                pass_pos.add((x,y))

    # while문 빠져나올때의 시간이 가장 빠르게 내려오는 시간
    print(f'#{tc} {t}')





