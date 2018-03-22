# coding = utf-8

'''
问题描述：
扑克牌分为红色和黑色，随机取扑克牌中一部分牌，一次正面展示：
求连续一段牌内，两种颜色牌数目相等的最大张数。
RBRRRR[R[[RBB]R]]
4
'''

def solve(A):
    countR, countB = 0, 0
    dif = []
    for a in A:
        if a == 'R':
            countR += 1
        else:
            countB += 1
        dif.append(countR - countB)

    difdict = {}
    maxr = 0
    for idx, d in enumerate(dif):
        if d in difdict:
            maxr = max(maxr, idx-difdict[d])
        else:
            difdict[d] = idx
    
    return maxr

res = solve('RBRRRRRRBBR')
print(res)
