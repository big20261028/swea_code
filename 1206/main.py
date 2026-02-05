

def main_logic():
    n = int(input())
    height_list = list(map(int,input().split()))

    total = 0
    for i in range(2,n-2):
        #print(height_list[i])
        #print(type(height_list[i]))
        left_view = max(height_list[i-2],height_list[i-1])
        right_view = max(height_list[i+2], height_list[i+1])

        good_home = min(height_list[i]-left_view,height_list[i]-right_view)
        if good_home > 0:
            total += good_home
    
    return total

result = ""
for num in range(1,11):
    total = main_logic()
    result += f"#{num} {total}\n"

print(result)

