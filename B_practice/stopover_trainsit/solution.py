from collections import defaultdict
from heapq import heappush,heappop
# 도시 개수
n = 0

# 무한변수
INF = float('inf')

# 지점마다 연결된 도로 정보
# 출발 도시 : [ (도착도시, 중량), .... ]
point_paths = defaultdict(list)

# 다익스트라 함수
def dijkstra(start_node):
    max_w_list = [0] * n
    max_w_list[start_node] = INF
    pq = [(-INF, start_node)]
    while pq:
        weight, st_node = heappop(pq)
        weight = -weight
        if weight < max_w_list[st_node]:
            continue

        for (end_node, need_w) in point_paths[st_node]:
            next_w = min(need_w,weight)
            if max_w_list[end_node] < next_w:
                max_w_list[end_node] = next_w
                heappush(pq, (-next_w, end_node))
    return max_w_list


'''
N개의 도시가 주어진다. 각 도시는 0부터 N-1까지 ID값을 가진다.
K개의 양방향 도로 정보가 주어진다. 각 도로마다 연결된 2개의 도시와 도로를 이용할 수 있는 최대 중량이 주어진다.
2개의 도시를 연결하는 도로는 1개만 주어진다.
도로와 연결된 2개의 도시가 서로 같은 경우는 없다.

Parameters
N: 도시의 개수 ( 5 ≤ N ≤ 1,000 )
K: 도로의 개수 ( 2 ≤ K ≤ 2,000 )
'''
def init(N, K, sCity, eCity, mLimit):
    global n, point_paths
    n = N
    point_paths = defaultdict(list)

    for i in range(K):
        point_paths[sCity[i]].append((eCity[i], mLimit[i]))
        point_paths[eCity[i]].append((sCity[i], mLimit[i]))

'''
sCity 도시와 eCity 도시를 연결하는 양방향 도로를 추가한다.
도로를 이용할 수 있는 최대 중량은 mLimit이다.
init()에 없던 새로운 도시는 주어지지 않는다.
sCity와 eCity를 연결하는 도로가 이미 존재하는 경우는 없다.
sCity와 eCity가 서로 같은 경우는 없다.

Parameters
sCity: 도로와 연결된 도시 ( 0 ≤ sCity < N )
eCity: 도로와 연결된 도시 ( 0 ≤ eCity < N )
mLimit: 도로를 이용할 수 있는 최대 중량 ( 1 ≤ mLimit ≤ 30,000 )
'''
def add(sCity, eCity, mLimit):
    point_paths[sCity].append((eCity, mLimit))
    point_paths[eCity].append((sCity, mLimit))

'''
M개의 경유지가 mStopover 배열로 주어진다.
sCity에서 M개의 경유지를 거쳐서 eCity까지 운송할 수 있는 화물의 최대 중량을 반환한다.
sCity와 eCity가 서로 같은 경우는 없다.
M개의 경유지가 서로 같은 경우는 없다.
경유지가 sCity나 eCity와 동일한 경우는 없다.

Parameters
sCity: 출발 도시 ( 0 ≤ sCity < N )
eCity: 도착 도시 ( 0 ≤ eCity < N )
M: 경유지 개수 ( 1 ≤ M ≤ 3)

(0 ≤ i ＜ M)인 모든 i에 대해,
mStopover[i]: 경유해야 되는 도시 ( 0 ≤ mStopover[i] < N )

Returns
sCity에서 M개의 경유지를 거쳐서 eCity까지 이동이 가능하다면, 운송할 수 있는 화물의 최대 중량을 반환한다.
불가능하다면, -1을 반환한다.
'''
def calculate(sCity, eCity, M, mStopover):
    arr = [sCity] + mStopover[:] + [eCity]
    arr_size = len(arr)

    max_weights = []
    for node in arr:
        max_weights.append(dijkstra(node))

    min_weight = INF
    flag = True
    for i in range(arr_size - 1):
        st_node = arr[i]
        end_node = arr[i+1]
        # 두 지점을 방문하는 경로가 운송가능한 최대 중량
        w = max_weights[i][end_node]
        if w == 0:
            flag = False
            break
        min_weight = min(min_weight, w)

    if flag:
        return min_weight
    else:
        return -1



