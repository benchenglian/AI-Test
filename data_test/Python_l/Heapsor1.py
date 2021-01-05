# 思路：
#
# 1.建立堆
#
# 2.得到堆顶元素，为最大元素
#
# 3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
#
# 4.堆顶元素为第二大元素。
#
# 5.重复步骤3，直到堆变空。
import random


def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j] > data[j + 1]:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp > data[j]:
            data[i] = data[j]   # 将父节点替换成新的子节点的值
            i = j   # 变成新的父节点
            j = 2 * i + 1   # 新的子节点
        else:
            break
    data[i] = tmp   # 将替换的父节点值赋给最终的父节点


def heap_sort(data):
    n = len(data)
    # 创建堆
    for i in range(n//2-1, -1, -1):
        sift(data, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):    # 从大到小
        data[0], data[i] = data[i], data[0]     # 将最后一个值与父节点交互位置
        sift(data, 0, i-1)


li = list(range(10))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)