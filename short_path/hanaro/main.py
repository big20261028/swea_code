import sys
sys.stdin = open('re_sample_input.txt', 'r')

from collections import defaultdict
from heapq import heappush, heappop, heapify

def find_short_path(st_node):
    visited = set()
    min_paths = list(path_infos[st_node])
    heapify(min_paths)
    #total_dist = []
    total_price = 0
    visited.add(st_node)

    while min_paths:
        dist, node = heappop(min_paths)
        if node in visited:
            continue

        visited.add(node)
        #total_dist.append(dist)
        total_price += E * dist

        for next_dist, next_node in path_infos[node]:
            if next_node in visited:
                continue
            heappush(min_paths, (next_dist, next_node))
    return total_price

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    island_x_vals = list(map(int, input().split()))
    island_y_vals = list(map(int, input().split()))
    #island_poses = [ list(map(int, input().split())) for _ in range(N) ]
    E = float(input())

    # 각 섬 사이의 거리 구하기
    # 각 섬은 0~N-1 번호를 매겨서 인덱스로 관리
    path_infos = defaultdict(list)
    for i in range(N):
        ix, iy = island_x_vals[i], island_y_vals[i]
        for j in range(i+1,N):
            jx, jy = island_x_vals[j], island_y_vals[j]
            mht_dist = (ix - jx)**2 + (iy - jy)**2
            # 최단거리 탐색을 위한 heappush
            # heappush(path_infos[i], (mht_dist, j))
            # heappush(path_infos[j], (mht_dist, i))
            path_infos[i].append((mht_dist, j))
            path_infos[j].append((mht_dist, i))

    #print(path_infos)
    min_prise = find_short_path(0)

    result = int(min_prise + 0.5)
    print(f'#{tc} {result}')