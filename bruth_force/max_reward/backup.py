import sys
sys.stdin = open('input.txt','r')

'''
원래가 가장 큰 값이어도 반드시 횟수만큼 교환을 해야함
오히려 작은 값이 될 가능성이 있음
만약 현재가 가장 큰 값일때, 남은 횟수가 홀수라면, 인덱스 끝자리와 끝자리 바로 앞을 한번 바꾸고 종료
'''

# 뒤에서부터 인덱스 탐색하며 일치하는 인덱스 값 return하는 함수
def find_index_reverse(target,arr):
    index = len(arr)
    for num in arr[::-1]:
        index -= 1
        if num == target:
            return index
    return -1


T = int(input())
for tc in range(1,T+1):
    number,r = input().split()
    r = int(r)
    # print(number)
    # print(r)

    num_list = list(map(int,number))

    # 가장 큰 값을 인덱스 0으로 옮기기
    # 횟수 1회 추가,

    for i in range(len(num_list)-1):
        target = num_list[i+1:]
        target_max = max(target)
        target_idx = find_index_reverse(target_max, num_list)
        # target_idx = num_list.index(max(target))
        if num_list[i] < target_max:
            num_list[target_idx] = num_list[i]
            num_list[i] = target_max
            r -= 1
        if not r :
            break

    if r > 0 and r % 2 == 1:
        a_idx = -1
        b_idx = -2
        # -1 인덱스가 -2보다 크지 않으면 교
        # 같은 숫자가 있다면 그 숫자 둘이 교환
        for i in range(10):
            if num_list.count(i) >= 2:
                a_idx = num_list.index(i)
                b_idx = find_index_reverse(i,num_list)
                break

        # last_num = num_list[a_idx]
        # next_num = num_list[b_idx]
        num_list[a_idx], num_list[b_idx] = num_list[b_idx], num_list[a_idx]

    # # 계산
    # price = 0
    # for i,num in enumerate(num_list[::-1]):
    #     price += num * (10 ** i)

    print(f'#{tc} {"".join(map(str,num_list))}')




