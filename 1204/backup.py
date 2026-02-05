'''
# 입력값 받기
end_num = int(input())
start_num = int(input())
scores_list = list(input().split())

# 받은 값 테스트
#print(n)
#print(start_num)
#print(score_list)

# score_list 안의 값을 dict에 등록
# 이미 등록되어 있다면 value에 +1

scores_dict = {}

for score in int(scores_list):
    if score in scores_dict:
        scores_dict[score] += 1
    else:
        scores_dict[score] = 1

# 테스트
#print(scores_dict)

# dict의 value 중 가장 값이 큰 순서대로 정렬
# 정렬을 위해 sorted 함수 사용
# value 값으로 정렬하기 위해 key 매개변수에 lambda 함수 사용
# 내림차순(큰거부터) 정렬을 위해 reverse=True 매개변수 사용

def do_sort(x):
    
    pass

sorted_scores_dict = dict(sorted(scores_dict.items(),key=lambda x : x[1], reverse=True))
print(sorted_scores_dict)

# 최종출력
for key in sorted_scores_dict.keys():
    print(f"#{start_num} {key}")
    start_num += 1
    if start_num > end_num:
        break

# 오답노트
"""
 - value가 같을때, 키 값이 큰 순서대로 출력해야 한다.
"""
'''
