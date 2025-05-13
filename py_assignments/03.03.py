#armstrong number
def check_armstrong(num):
    sum=0
    temp=num
    str_num=str(num)
    while num>0:
        digit=num%10
        sum+=digit**len(str_num)
        num //=10
    if temp==sum:
        return True
    else:
        return False

num=int(input("enetr a number"))
print(check_armstrong(num))

# write a program that finds the smallest prime digit (2, 3, 5, or 7) in a given number.
def smallest_prime_digit(n):
    prime_digits={'2','3','5','7'}
    digits=(str(n))
    primes_in_number=[]
    for d in digits:
        if d in prime_digits:
            primes_in_number.append(int(d))
    
    if primes_in_number:
        return min(primes_in_number)
    else:
        return "no prime found in number"
    

n=int(input("enter a number: "))
print(smallest_prime_digit(n))
