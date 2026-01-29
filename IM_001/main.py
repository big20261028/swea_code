a = int(input())

for _ in range(a):
    N = int(input())
    map_data = [ list(map(int,input().split())) for _ in range(N) ]

    top_position_list = []
    top_height  = map_data[0][0]

    for idx_y, item in enumerate(map_data):
        for idx_x, n in enumerate(item):
            if n > top_height:
                top_height = n
                top_position_list.clear()
                top_position_list.append((idx_y,idx_x))
            elif n == top_height:
                top_position_list.append((idx_y,idx_x))

    print(top_position_list)