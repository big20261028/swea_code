import sys
sys.stdin = open('Sample_input.txt','r')

def tool(odd,even):
    while True:
        if odd > even+1:
            odd -= 2
            even += 1
            if even-1 <= odd <= even+1:
                return odd,even
        elif even > odd+1:
            odd += 2
            even -= 1
            if odd-1 <= even <= odd+1:
                return odd,even
        else :
            return odd, even



import math
T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))

    max_h = max(arr)

    # 각 나무를 %3 하고 나온 나머지가 1이면 딕셔너리 1에 추가 2면 2에 추가
    #need_dict = {'1':0, '2':0}
    odd = 0
    even = 0

    for tree in arr:
        half = (max_h-tree)//3
        tip = (max_h-tree) % 3
        odd += half
        even += half
        if tip == 1:
            odd += 1
        elif tip == 2:
            even += 1

    #print(odd,even)
    odd,even = tool(odd,even)

    if odd < even :
        day = odd+even + 1
    else:
        day = odd + even

    print(f'#{test_case} {day}')
    #print(odd,even)
