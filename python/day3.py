str1='hello'
str2='hello'
# str1[1]='a'
print(str1)


#sets
set1={1,2,5,8,0.9,2,4,5,8,"true","hey",False}
print(set1)

#dictionary
dict1={}
print(type(dict1))

dict2={1:"sath" , 2:"wika",3:"beth"}
print(dict2[3])

dict2[3]="bethu"
print(dict2[3])

#none
str1=None
print(type(str1))
print(str1)
print(id(str1))

# complex into boolean
num1=3+8j
print(bool(num1))
num1=0+8j
print(bool(num1))
num1=0+0j
print(bool(num1))
# num1=0i
print(bool(num1))

# input from user
num1=int(input("enter a number"))
num2=int(input("enter another number"))
print(num1+num2)

print(True and True)
print(True and False)
print(5>7 and 4<5)
print(4 and 5)
print(0 and 2)
print(2 and 0)
print(-4 and -5)
print(0 and False)

#bitwise operators
binary_num1=bin(21)
binary_num2=bin(12)
print(binary_num1 and binary_num2)