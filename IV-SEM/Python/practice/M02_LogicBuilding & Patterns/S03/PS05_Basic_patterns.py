'''1)input:4
  output:****
         ****
         ****
         ****


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''

'''
2)n=4
*
**
***
****
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''
'''n=4
   A
   A B
   A B C
   A B C D
'''
'''n=3
   ***
   * *
   ***
'''
'''m=4
   1
   2 3
   4 5 6
   7 8 9 10'''
'''staircase in hackerrank'''
'''
     *
    *  *
  *   *  *
*  *   *   *
  *   *   *
    *   *
      *
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''
''' 
     1
    1  2
   1 2   3
1    2  3   4'''
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))"""

n=int(input())
val=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(val),end=" ")
        val+=1
    print()