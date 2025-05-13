# perfect number
num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# lcm of two numbers
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
max_num=min(num1,num2)
while True:
    if max_num%num1==0 and max_num%num2==0:
        print(" The LCM of", num1, "and", num2, "is: ", i)
        break
    max_num+=1



# sum of non prime digits
number=input("enter a number:")
non_prime_sum=0
for digit in number:
    d=int(digit)
    if d not in [2,3,5,7]:
        non_prime_sum+=d
print("sum of non-prime digits:",non_prime_sum)