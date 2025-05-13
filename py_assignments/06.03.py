# 

sum1=0
sum2=0
list1=[2,1,4,5,6]
for i  in range(len(list1)):
    print(list1[i])
    sum1+=list1[i]
print(sum1)


i=0
while i<len(list1):
    sum2+=list1[i]
    # print(i)
    print(list1[i])
    i+=1
print(sum2)