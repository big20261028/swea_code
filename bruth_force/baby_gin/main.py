import sys
sys.stdin = open('input.txt','r')

from itertools import permutations

def is_continue(item):
    return item[0]+1 == item[1] and item[1]+1 == item[2]

def is_same(item):
    return item[0] == item[1] and item[1] == item[2]

T = int(input())
for tc in range(1,T+1):
    num_list = list(map(int,input().strip()))

    targets = permutations(num_list,6)


    flag = False
    for tg in targets:
        a = tg[:3]
        b = tg[3:]
        if (is_same(a) or is_continue(a)) and (is_same(b) or is_continue(b)):
            flag = True
            break

    if flag :
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')