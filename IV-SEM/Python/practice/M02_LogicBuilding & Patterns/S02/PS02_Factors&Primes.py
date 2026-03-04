"""n=int(input())
counter=0
for i in range(1,n//2+1):
    if n%i==0:
        counter+=1  
print(counter+1)"""

'''n=int(input())
counter=0
for i in range(2,n//2+1):
    if n%i==0:
        counter+=1
print("Prime" if counter==1  else "Not Prime")'''

'''n=int(input())
fact=1
for i in range(n,1,-1):
    fact*=i
print("factorial is",fact)'''

'''
n=int(input())
if n<0:
    print("Factorial is not defined for negative numbers")
elif n==0 or n==1:
    print(1)
else:
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial is",fact)'''

#gcd of 2 numbers:
a=int(input())
b=int(input())
while b:
    a,b=b,a%b
print(a)


import math
print(math.gcd(a,b))