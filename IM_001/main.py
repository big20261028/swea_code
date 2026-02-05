T = int(input())

for _ in range(T):
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
    print("맵 생성 완료")
    print("출발지점 좌표 :",top_position_list)
    
    result = 0
    for pos in top_position_list:
        move_cnt = 0
        while True:
            dir_dict = {
                'w' : top_height,
                'e' : top_height,
                's' : top_height,
                'n' : top_height
            }
            for key in dir_dict:
                if pos[1] == 0 or pos[1] == (N-1) or pos[0] == 0 or pos[0] == (N-1):
                    pass
                else:
                    if key == 'w': dir_dict[key] = map_data[pos[0]][pos[1]-1]
                    if key == 'e': dir_dict[key] = map_data[pos[0]][pos[1]+1]
                    if key == 's': dir_dict[key] = map_data[pos[0]-1][pos[1]]
                    if key == 'n': dir_dict[key] = map_data[pos[0]+1][pos[1]]
                
            min_height = top_height
            for val in dir_dict.values():
                if min_height > map_data[val[0]][val[1]]:
                    min_height = map_data[val[0]][val[1]]
                    
            
            
            
            # w, e, s, n = map_data[pos[0]][pos[1]]
            # if pos[1] == 0:
            #     w = map_data[pos[0]][pos[1]]
            # else:
            #     w = map_data[pos[0]][pos[1]-1]
            
            # if pos[1] == (N-1):
            #     e = map_data[pos[0]][pos[1]]
            # else:
            #     e = map_data[pos[0]][pos[1]+1]
                
            # if pos[0] == 0:
            #     n = map_data[pos[0]][pos[1]]
            # else:
            #     n = map_data[pos[0]-1][pos[1]]
                
            # if pos[0] == (N-1):
            #     s = map_data[pos[0]][pos[1]]
            # else:
            #     s = map_data[pos[0]+1][pos[1]]
                
            # print('현재 위치 기반 사방향 데이터 설정')
            # if 
            
            
            
        
                
                
        
    
