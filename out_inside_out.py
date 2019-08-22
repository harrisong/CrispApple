import math

def inside_out(strin):
    mid = len(strin)/2
    first = ""
    second = ""
    if mid % 2 == 0:
        for i in range(int(mid)):
            first = strin[i] + first
            second = second + strin[i+int(mid)]
    else:
        strin = strin + strin[math.floor(mid)]
        mid = math.ceil(mid)
        for i in range(int(mid)):
            first = strin[i] + first
            second = second + strin[i+mid]
    return first + second


print(inside_out("abcd"))





