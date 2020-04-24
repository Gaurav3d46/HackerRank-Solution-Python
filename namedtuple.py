from collections import namedtuple
n=int(input())
field=input().split()
sum=0
r=namedtuple('a',fiel
for i in range(n):
    f1,f2,f3,f4=input().split()
    a=r(f1,f2,f3,f4)
    sum+=int(a.MARKS)
c=(sum//n)
print("{:.2f}".format(c))
