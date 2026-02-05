### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    #N = int(input())
    text = input()
    char_dict = { 'b':'d',"d":"b",'p':'q','q':'p'}
    result = [ char_dict[char] for char in text[::-1] ]
    result = ''.join(result)
    print(f"#{test_case} {result}")
