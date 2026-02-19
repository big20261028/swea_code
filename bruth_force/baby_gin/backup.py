import sys
sys.stdin = open('input.txt','r')

from itertools import permutations
from itertools import combinations

T = int(input())
for tc in range(1,T+1):
    num_list = list(map(int,input()))

    # 리스트 6개 중, 3개를 골라오기
    # 그 객체가 연속되는지, 동일한지 확인
    # 해당된다면 해당 객체 값을 set에 저장
    # set의 길이가 6이라면 true
    pass_num = set()
    targets = combinations(num_list,3)

    # 변경사항
    # 골라온 3개와 안골라온 3개가 모두 run or triplet 이어야 유효

    for items in targets:
        items = list(items)
        another_items = [ num for num in num_list if num not in items ]
        items.sort()
        if items[0] == items[1] and items[1] == items[2]:
            for a in items:
                pass_num.add(a)
        if items[0] + 1 == items[1] and items[1]+1 == items[2]:
            for a in items:
                pass_num.add(a)

    print(pass_num)

    # set에 모든 num_list의 객체가 있으면 true
    # 아니면 false
    flag = True
    for num in num_list:
        if num not in pass_num:
            flag = False

    if flag:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')
