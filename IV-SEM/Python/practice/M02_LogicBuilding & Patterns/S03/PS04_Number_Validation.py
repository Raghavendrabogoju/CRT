'''1)Armstrong Number:
input:153
output:Armstrong Number

input:24
output:not an Armstrong number'''
'''
n=int(input())
count=len(str(n))
sum=0
for digit in str(n):
    sum+=int(digit)**count
print("Armstrong number" if sum==n else "not an Armstrong number")'''

'''
#2)perfect number code :
n=int(input())
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=i
print("perfect number" if count==n else "not a perfect number")'''
 
'''Strong number:
input:123
output:not a strong number 
Explanation:1!+2!+3!=1+2+9
'''
def factorial(n):
    if n<0:
        return "no factorial for -ve "
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact
n=int(input())
s=0
for digit in str(n):
    s+=factorial(int(digit))
print("Strong number" if s==n else "Not a strong number")