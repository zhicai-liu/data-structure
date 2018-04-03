# coding = utf-8

'''
1.插入排序
基本思想：将一个个元素插入已排序序列的正确位置,并维持其余元素的正确顺序。
初始化序列为第一个元素的序列。
'''

def insert_sort(lst):
    for i in range(1, len(lst)):  # 第一个元素为初始的已排序序列
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]   # 从后往前逐个比较，逐个将大元素后移，确定插入位置。
            j -= 1
        lst[j] = x
    return lst

# res = insert_sort([3, 2, 4, 5, 7, 2, 1])
# print(res)


'''
单链表实现插入排序

'''


















'''
2.选择排序
基本思想：按顺序选出此时序列中的最小元素。
'''

def select_sort(lst):
    for i in range(len(lst)-1):
        k = i
        for j in range(i+1, len(lst)): # k为已知最小元素的位置
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]
    return lst

# res = select_sort([3, 1, 4, 5, 7, 2, 1])
# print(res)


'''
3.堆(选择)排序（一种高效的选择排序算法）
基本思想：
优先队列是一种缓存结构，像栈和队列一样，可以保存、访问、弹出元素，最重要的特点是存入其中的每项数据都附有一个数值，表示这个项的优先程度。
堆是采用树形结构实现优先队列的一种方式，从结构上它就是一颗完全二叉树，但是它满足一种特殊的堆序：任一节点的优先级高于或者等于其子节点的优先级
'''

def heap_sort1(lst):        # 采用小顶堆
    '''
    向下筛选:将待归位的元素e（堆顶元素）与左右子节点（子堆）比较，将三者最小的值放到堆顶，若e最小直接放到堆顶，排序完成；
    若不是，则必为子节点中的一个，将其中一个放到堆顶后，空出的位置又形成了以上情形，不断进行以上操作，使回归堆序。
    '''
    def siftdown(lst, e, begin, end):
        i, j = begin, begin*2 + 1            # i表示父节点，j表示左子节点，lst[i]始终代表空位置，找到小节点并放到该位置。
        while j < end:
            if j+1 < end and lst[j+1] < lst[j]:      # 如果右子节点存在，并且右子节点小于左子节点，那么将j加1，此时lst[j]为右子节点
                j += 1                               
            if e < lst[j]:                   # 若e在三者中最小，跳出循环，把e放到堆顶
                break 
            lst[i] = lst[j]                  # 若e不是最小，因为lst[j]始终代表左右子节点中较小的一个，则lst[j]最小，放到空位置lst[i]，此时j位置为空，将其赋给i。
            i, j = j, 2*j + 1                # 更新父节点和左子节点指针，进行下一次的筛选，直到堆更新完成
        lst[i] = e
    
    end = len(lst)
    for i in range(end//2, -1, -1):          # 建堆，从end//2位置开始，后面的元素都是二叉树的叶节点，叶节点视为已排序，前面的每一个元素lst[i]在已排序的树上向下筛选
        siftdown(lst, lst[i], i, end)
    for i in range((end-1), 0, -1):          # 建堆完成后，循环取出最小元素（堆顶），将其积累在表的最后，然后拿着最后的元素做一次向下筛选，使回归堆序。
        e = lst[i]
        lst[i] = lst[0]                      # 将最小元素（第一个元素），放到最后一个位置
        siftdown(lst, e, 0, i)               # 将取出的最后一个元素e进行一次向下筛选
    return lst[::-1]                         # 采用小顶堆时，最后lst为从大到小排序，要想从小到大输出，需要反转一下。

    


# lst = [9, 2, 8, 5, 3, 6, 2]
# res = heap_sort1(lst)
# print(res)



def heap_sort2(lst):             # 采用大顶堆
    

    def siftdown(lst, e, begin, end):
        i, j = begin, 2*begin + 1
        while j < end:
            if j+1 < end and lst[j+1] > lst[j]:
                j += 1
            if e > lst[j]:
                break 
            lst[i] = lst[j]
            i, j = j, 2*j + 1
        lst[i] = e

    end = len(lst)
    for i in range(end//2, -1, -1):
        siftdown(lst, lst[i], i, end)
    for i in range((end-1), 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i)

    return lst 


# lst = [9, 2, 8, 5, 3, 6, 2]
# res = heap_sort2(lst)
# print(res)









'''
4.交换排序（冒泡排序）
基本思想：不断减少序列中的逆序，每一趟比较都将最大元素”沉底“。
不断比较相邻元素，发现逆序就交换彼此。
'''

# 原始版

def bubble_sort0(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

# res = bubble_sort0([1, 4, 2, 5, 8, 3])
# print(res)

# 改进版：
# 只有序列中的最小元素在最末尾时，才需要循环len(lst)次
# 如果在一次扫描中没有发现逆序就直接跳出循环

def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break
    return lst

# res = bubble_sort([1, 4, 5, 2, 3, 9, 5])
# print(res)


'''
5.快速排序
基本思想：按某种标准（第一个元素）将序列划分为‘小序列’和‘大序列’，
从左往右的顺序为小序列、分界、大序列，
然后递归地将小序列和大序列进行划分，
直到划分后的大、小序列只剩一个元素，则排序完成。
'''

def qsort_rec(lst, l, r):    # l为lst中的第一个位置，r为lst中最后一个位置
    if l>=r: return 
    i = l
    j = r
    pivot = lst[i]           # pivot为划分标准，为lst第一个元素
    while i < j:
        while i < j and lst[j] >= pivot:
            j -= 1           # 用j向左扫描找小于pivot的元素
        if i < j:
            lst[i] = lst[j]
            i += 1           # 小元素移到左边
        while i < j and lst[i] <= pivot:
            i += 1           # 用i向右扫描找大与pivot的元素
        if i < j:
            lst[j] = lst[i]
            j -= 1           # 大元素移到右边
    lst[i] = pivot           # 将pivot放到中间i=j的位置
    qsort_rec(lst, l, i-1)   # 递归处理左半区间
    qsort_rec(lst, i+1, r)   # 递归处理右半区间
    return lst
    
# lst = [9, 4, 5, 2, 1, 6 ,7, 2]
# res = qsort_rec(lst, 0, len(lst)-1)
# print(res)


'''
快速排序的另一种实现
基本思想：同样是递归处理，不同的元素存放顺序不同，之前是小元素、未检查元素、大元素，
现在是小元素、大元素、未检查元素，
用两个下标变量，i的值总是最后一个小元素的下标，j的值是第一个未检查元素的下标。
如果j较大，直接将j的值加1；
如果j较小，将i+1，然后交换i和j的值
'''


def quick_sort(lst, begin, end):
    if begin >= end: return 
    pivot = lst[begin]                       # 以第一个元素为比较标准
    i = begin                                # i始终指向最后一个小元素，从第一个元素开始。
    for j in range(begin+1, end+1):          # end为最后一个元素的下标
        if lst[j] < pivot:                   # 发现小元素，开始交换，如果不是小元素，直接执行下一次循环，j加1
            i += 1
            lst[i], lst[j] == lst[j], lst[i] # 因为i指向最后一个小元素，i+1为大元素，所以交换后，直接j+1检查下一个元素
    # lst[i], pivot = pivot, lst[i]          # pivot只是lst[begin]的引用，此语句不改变lst本身！！  
    lst[begin], lst[i] = lst[i], lst[begin]  # 循环结束后，小元素在前，大元素在后，将lst[begin]与最后一个小元素lst[i]交换后，就实现了pivot之前是小元素，其后是大元素。

    quick_sort(lst, begin, i-1)              # pivot与lst[i]交换之后，pivot在i位置上
    quick_sort(lst, i+1, end)
    return lst 

# lst = [9, 1, 5, 3, 6 ,2, 7]
# res = quick_sort(lst, 0, len(lst)-1)
# print(res)



'''
6.归并排序
基本思想：
不断将两个相邻有序序列合并为一个有序序列；
反复复制两个子序列首元素中较小的值；
有序子序列不断变长，最终变成一个有序序列，排序完成。
'''

# 最下层：实现表中相邻的两个子序列的归并，按顺序存入另一个缓存表

def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low           # i为第一段下标，j为第二段下标，k为lto的下标
    while i < mid and j < high:       # 反复复制两分段首记录中较小的
        if lfrom[i] < lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:                   # 复制第一段中剩余的记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:                  # 或复制第二段中剩余的记录
        lto[k] = lfrom[j]
        j += 1
        k += 1

# 中间层：顺序进行各对有序序列的归并，完成一趟排序，并将结果顺序存入缓存表中

def merge_pass(lfrom, lto, llen, slen):                # llen为表长度，slen为分段长度
    i = 0
    while i + 2*slen < llen:                           # 归并长slen的两段
        merge(lfrom, lto, i, i+slen, i+2*slen)            
        i += 2*slen                                    # 完成一对子序列的排序，更新下标，完成下一对子序列的排序
    if i+slen < llen:                                  # 剩下两段，后一段长度小于slen
        merge(lfrom, lto, i, i+slen, llen)
    else:                                              # 只剩下一段，复制到表lto
        for j in range(i, llen):
            lto[j] = lfrom[j]

# 最高层：完成一趟排序，将分段长度乘以2，再进行相邻子序列的归并，不断执行此操作，直至slen长度大于llen，则退出循环,排序完成。

def merge_sort(lst):
    slen, llen = 1, len(lst)                         # 初始化slen为1，即相邻两个元素排序
    templst = [None]*llen 
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)         # 即使最终结果存在templst中，执行完此操作又会将结果还给lst，具体为直接执行merge_pass函数的else语句。
        slen *= 2
    return lst  

# lst = [9, 1, 4, 2, 6, 3, 7, 5]
# res = merge_sort(lst)
# print(lst)



'''
7.希尔排序
基本思想：
插入排序的一种,又叫“缩小间隔排序”，目的是减少排序次数。
用一个划分间隔i，
将源列表划分为若干子列表，对每个子列表进行插入排序。
不断减小i，
当i为1时，就是原始的插入排序。
当i变化时，不会改表之前排好序的序列。
最坏的情况是，只有最后当i为1时，排序才起作用，之前的间隔排序不起作用。
'''

def shellsort(lst):
    gap = len(lst)//2               # 刚开始把源列表分为两份，得到间隔gap                              

    while gap > 0:
        for start in range(gap):                   # 每一种gap的情况下，是要往后推移的
            insert_sort(lst, start, gap)           # start : 一种间隔不只有一次插入排序，例如lst[1]lst[3]lst[5]做一次排序，lst[2]lst[4]lst[6]再做一次排序……
        print("After increments of size", gap, "The list is", lst)
        gap = gap // 2      # gap也来越小，直到gap=1

def insert_sort(lst, start, gap):                        # 确定好间隔之后，接下来的操作就是原始的插入排序。
    for i in range(start+gap, len(lst), gap):            # 插入排序是从当前位置跟前一个位置比较，从后往前操作。
        currentvalue = lst[i]                            # i为当前位置的下标
        
        while i >= gap and lst[i-gap] > currentvalue:    # 不断拿当前值跟前一个数比较
            lst[i] = lst[i-gap]
            i = i-gap 
            lst[i] = currentvalue 

lst = [9, 1, 6, 2 ,7, 3, 8, 5]
shellsort(lst)
print(lst)










'''
8.桶排序
'''

'''
9.基数排序
'''


'''
10.计数排序
'''

'''
11.二分插入排序
'''

'''
12.表插入排序
'''


'''
13.蒂姆排序
'''
