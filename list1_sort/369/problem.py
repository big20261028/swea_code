### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
n = int(input())
for i in range(1,n+1):
    text = str(i)
    if "3" in text or "6" in text or "9" in text :
        cnt = text.count("3") + text.count("6") + text.count("9")
        print("-"*cnt, end=" ")
        continue
    print(i,end=" ")