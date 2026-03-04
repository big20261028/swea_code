import sys
sys.stdin = open('sample_input.txt', 'r')

direction_filter = {
    1 : 0,
    2 : 2,
    3 : 1,
    4 : 3
}

# ( 상: 0, 좌: 1, 하: 2, 우: 3 )
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

T = int(input())
for tc in range(1,T + 1):
    N, M, K = map(int,input().split())

    micros = {}
    for _ in range(K):
        # 이동방향 : ( 상: 1, 하: 2, 좌: 3, 우: 4 )
        # 필터 써서 계산하기 편하게 변경
        # ( 상: 0, 좌: 1, 하: 2, 우: 3 )
        x, y, power, dist = map(int,input().split())
        micros[(x, y)] = {
            'power': power,
            'max_p': power,
            'dist': direction_filter[dist]
        }

    # print(micros)

    t = 0
    while t < M:
        t += 1
        temp_dict = {}
        for (x, y), micro in micros.items():
            dx, dy = dxy[micro['dist']]
            nx, ny = x + dx, y + dy
            # 좌표값이 x가 0이거나 N-1일때
            # 좌표값이 y가 0이거나 N-1일때
            if nx == 0 or nx == (N-1) or ny == 0 or ny == (N-1):
                remain_power = micro['power'] // 2
                if remain_power:
                    temp_dict[(nx, ny)] = {
                        'power': remain_power,
                        'max_p': remain_power,
                        'dist': (micro['dist'] + 2) % 4
                    }
            elif (nx, ny) in temp_dict:
                temp_dict[(nx, ny)]['power'] += micro['power']
                if micro['power'] > temp_dict[(nx, ny)]['max_p']:
                    temp_dict[(nx, ny)]['dist'] = micro['dist']
                    temp_dict[(nx, ny)]['max_p'] = micro['max_p']
            else:
                temp_dict[(nx, ny)] = {
                    'power': micro['power'],
                    'max_p': micro['power'],
                    'dist': micro['dist']
                }
        micros = temp_dict

    total = 0
    for micro in micros.values():
        total += micro['power']

    print(f'#{tc} {total}')


