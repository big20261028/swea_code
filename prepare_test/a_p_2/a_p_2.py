import sys
sys.stdin = open('input1.txt','r')

from collections import deque

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    data_dict = {}
    for i in range(1,N+1):
        info = list(map(int,input().split()))
        count = info[0]
        if count == 0:
            data_dict[i] = [0]
        else:
            data_dict[i] = info[1:]

    success_list = [0]
    days = 0

    while data_dict:
        days += 1
        temp_list = success_list.copy()
        for key,value in data_dict.copy().items():
            cnt = 0
            for subject in value:
                if subject in success_list:
                    cnt += 1
            if cnt == len(value):
                temp_list.append(key)
                data_dict.pop(key)

        if len(success_list) == len(temp_list):
            days = -1
            break

        success_list = temp_list

    print(f'#{tc} {days}')


    lists.sort(key = lamda x : x[1])
