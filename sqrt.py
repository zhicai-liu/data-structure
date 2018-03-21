
# 问题描述：求一个输的平方根。

# 二分法逼近

def sqrt(n):
    y = n/2
    x = n ** 0.5
    up = n * 1.0
    low = 0.0
    while abs(y-x) > 0.0000000000000000000001:
        if y*y > n :
            up = y
            y = low + (y-low)/2

        else:
            low = y
            y = up - (up-y)/2

    return y 


# 牛顿法实现,直接利用迭代公式

def sqrt1(n):
    x = n ** 0.5
    y = n/2  # 先折半，减少迭代次数
    while abs(y-x) > 0.00000000000000001:
        y = (y+n/y)/2
    return y

print(sqrt1(9))


