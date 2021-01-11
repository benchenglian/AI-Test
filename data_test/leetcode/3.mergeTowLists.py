import re

l1 = "1->2->4"
print(re.sub("\D","",l1))
s1=re.sub("\D","",l1)
print("->".join(s1))

l2 = [1,2,5]
