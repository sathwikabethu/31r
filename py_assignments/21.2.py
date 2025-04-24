#  I.Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)
#     II. Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n=int(input("Enter a number:"))
print((n*n+1)/ 2)
# Print all even numbers between 1 and 50 using a while loop.
for i in range(1,51):
    if i%2==0:
        print(i)

# Write a program to display the multiplication table of a given number. First 20
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num ,"*",i, "=", (num*i))

# Write a program to calculate the factorial of a number using a while loop.
n=int(input("enter a number:"))
factorial=1
while n>0:
    factorial*=n
    n-=1
print(factorial)

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
print("Numbers that can be divisible by both 3 and 5 are:")
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)