import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import defaultdict

T = int(input())

# 0 상 / 1 좌 / 2 하 / 3 우
dir_filter = {
    1 : 0,
    2 : 2,
    3 : 1,
    4 : 3
}
dxy = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]
# (dir + 2) % 4

for tc in range(1, T+1):
    # 셀의 개수, 격리시간, 미생물 개수
    N, M, K = map(int,input().split())

    microbes = {}

    for _ in range(K):
        cell_x, cell_y, power, direction = map(int,input().split())
        changed_direction = dir_filter[direction]
        microbes[(cell_x, cell_y)] = {
            'power' : power,
            'dir' : changed_direction,
            'max_power' : power,
        }

    t = 0

    while t < M:
        t += 1

        next_microbes = {}

        for microbe_pos, microbe_info in microbes.items():
            c_x, c_y = microbe_pos
            c_power = microbe_info['power']
            c_dir = microbe_info["dir"]

            dx, dy = dxy[c_dir]
            nx, ny = c_x + dx, c_y + dy

            # 테두리에 위치했을 경우 미생물 수 /2 and 이동방향 반전
            if not (1 <= nx < N-1 and 1 <= ny < N-1):
                c_power //= 2
                if c_power == 0:
                    continue
                c_dir = (c_dir + 2) % 4

            # 다음에 이동할 셀에 미생물이 있으면
            if (nx, ny) in next_microbes:
                senior_microbes = next_microbes[(nx, ny)]

                if senior_microbes['max_power'] < c_power:
                    senior_microbes['dir'] = c_dir
                    senior_microbes['max_power'] = c_power

                senior_microbes['power'] += c_power
            # 미생물 없으면
            else:
                next_microbe = {
                    'power': c_power,
                    'dir': c_dir,
                    'max_power': c_power,
                }
                next_microbes[(nx, ny)] = next_microbe

        microbes = next_microbes

    result = 0
    for microbe_info in microbes.values():
        result += microbe_info['power']

    print(f'#{tc} {result}')








