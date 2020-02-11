import math

def is_smart_number(num):
    # cnt = 0

    # for i in range(1, num+1):
    #     if num % i == 0:
    #         cnt += 1

    # if cnt % 2 == 0:
    #     return False

    # return True

    v = int(math.sqrt(num))
    if num == v * v:
        return True
    
    return False


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")