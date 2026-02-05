# 입력값 받기
end_num = int(input())

# 최빈값을 찾는 함수
def many_call_score(scores_list):
    scores_set = set(scores_list)
    many_call_list = []
    max_count = 0

    for item in scores_set:
        if max_count < scores_list.count(item):
            max_count = scores_list.count(item)
            many_call_list = []
            many_call_list.append(item)
        elif max_count == scores_list.count(item):
            many_call_list.append(item)
        
    if len(many_call_list) > 1 :
        many_call_list.sort(reverse=True)
        
    # # 테스트
    # print("="*50)
    # print("max_count",max_count)
    # print("many_call_list",many_call_list)
    # print("="*50)

    return many_call_list[0]

result = ""

# 변수가 의미 없을때 _ 사용
for _ in range(0,end_num):
    num = int(input())
    scores_list = list(map(int,input().split()))

    # 함수로 최빈값 찾기
    score = many_call_score(scores_list)

    # num과 최빈값을 출력(여러개일 시 가장 큰 값 출력)
    result += f"#{num} {score}\n"
print(result)

# 오답노트
'''
 - value가 같을때, 키 값이 큰 순서대로 출력해야 한다.
 - input.txt 파일 확인 -> 입력값이 완전 다름
 - 처음 입력된 변수 만큼 for문 돌리고 안에서 input 값을 받아 가장 많이 입력된 값 출력하기(여러개일 경우 가장 큰 점수 출력)
 - max_count가 갱신될 때, 이전 데이터 초기화 필요
'''