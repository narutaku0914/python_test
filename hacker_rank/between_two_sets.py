import math
from functools import reduce

a = [1]
b = [100]

# 最小公倍数
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)    # math.gcdは最大公約数を求める

def getTotalX(a, b):
    if len(a) == 1:
        min_lcm = a[0]
    min_lcm = reduce(lcm_base, a, 1)
    lcm_list = [min_lcm * i for i in range(1, int(b[-1] / min_lcm) +1)]
    total = 0
    for lcm in lcm_list:
        ok = 0
        for num in b:
            if num % lcm ==0:
                ok += 1
        if ok == len(b):
            total += 1

    return total


print(getTotalX(a, b))
