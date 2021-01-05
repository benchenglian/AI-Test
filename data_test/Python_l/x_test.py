def xtest(num):
    if num == 1 :
        return 1
    return num+xtest(num-1)

print(xtest(10))

list_a = [3,6,4,2,11,10,5]
print(sorted(list_a))

strint_a = "what is your name"
list_b = strint_a.split()
#list_c=list_b[::-1]

print(" ".join(list_b[::-1]))