# coding = utf-8

'''
问题描述：
正整数A{i}代表x坐标i位置有一条垂直于坐标轴高度为A{i}的挡板，
问给定数组A，任选两个A{i}A{j}两个挡板，能盛装的最对的水的容器面积？
'''
def maxwater(A):
    start = 0
    end = len(A)-1
    if end == 0:
        return 0
    res = 0
    while start < end:
        res = max(res, (end-start)*min(A[start], A[end]))
        if A[start] < A[end]:
            start += 1
        else:
            end -= 1
    return res

res = maxwater([1,2,3,4,5,6])
print(res)
