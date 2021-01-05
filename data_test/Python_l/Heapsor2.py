import random


def random_list(n):
    '''
    生成随机数据
    :param n:
    :return:
    '''
    ret = []
    a1 = ['赵', '钱', '孙', '李', '邹', '吴', '郑', '王', '周']
    a2 = ['力', '好', '礼', '丽', '文', '建', '梅', '美', '高', '']
    a3 = ['强', '文', '斌', '阔', '文', '莹', '超', '云', '龙', '']
    ids = range(1001, 1001 + n)
    for i in range(n):
        name = random.choice(a1) + random.choice(a2) + random.choice(a3)
        age = random.randint(18, 60)
        dic = {'id': ids[i], 'name': name, 'age': age}
        ret.append(dic)
    return ret


def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j]['id'] < data[j + 1]['id']:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp['id'] < data[j]['id']:
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

li = random_list(1000) # 生成数据
random.shuffle(li) # 将数据打乱
heap_sort(li)
print(li)