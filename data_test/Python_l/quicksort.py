# 快排

#简单版
def quickSort(listx):
    if len(listx)<=1:
        return listx
    pivot = listx[len(listx)//2] # 取中间元素为比较数 pivot
    print("中间数",pivot)
    listl = [x for x in listx if x < pivot] # <pivot的放在一个列表
    print(listl)
    listm = [x for x in listx if x == pivot] # =pivot的放在一个列表
    print(listm)
    listr = [x for x in listx if x > pivot] # >pivot的放在一个列表
    print(listr)
    left = quickSort(listl)     #递归
    right = quickSort(listr)    #递归
    return left + listm + right  #整合
# a=quickSort([9,3, 6, 8, 9, 19, 1, 5])
# print(a)

sum = 0
n=1234
while n > 0 :
    sum += n % 10
    n = n // 10
    #print(n)
# print(sum)

def testsum(num):
    sum_s = 0
    while num > 0:
        sum_s += num % 10
        num = num // 10
    return sum_s
print(testsum(123))