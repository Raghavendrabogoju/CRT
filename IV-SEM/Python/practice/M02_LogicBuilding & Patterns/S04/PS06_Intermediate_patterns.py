'''li=[1,2,3,4,5]
output=[]
for i in li:
    output.append(i*4)
print(output)

print([i*2 for i in li])
'''
'''li=[1,2,3,4,5]
#output:[2,4]
res=[]
print([i for i in li if i%2==0])'''

'''#['a','b','c']==>"abc"
lis1=['a','b','c']
res=""
for ch in lis1:
    res+=ch
print(res)
print("".join(lis1))'''

n=4
for i in range(1,n+1):
        print((n-i)*' '+i*"* ")

