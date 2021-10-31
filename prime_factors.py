import math
number=12
number_copy=number
ans=[]
index=0
while number%2==0:
    ans.insert(index, 2)
    index+=1
    number=number/2
for i in range (3, number_copy, 2) :
    while number%i==0:
        ans.insert(index, i)
        index+=1
        number=number/i
print(ans)