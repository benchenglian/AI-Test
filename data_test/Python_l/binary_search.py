# 二分搜索是一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，
# 则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
# 如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(listx, x, y, z):
    # 基本判断
    if y >= x:
        mid = int(x + (y - x) / 2)
        # 元素整好的中间位置
        if listx[mid] == z:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif listx[mid] > z:
            return binarySearch(listx, x, mid - 1, z)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(listx, mid + 1, y, z)
    else:
        # 不存在
        return -1

# 测试数组
list_test = [2, 4, 6, 10, 40]

z = 10
# 函数调用
result = binarySearch(list_test, 0, len(list_test) - 1, z)
if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")

