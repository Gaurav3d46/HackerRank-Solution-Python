from collections import namedtuple
n=int(input())
sum=0
r=namedtuple('r','IDs MARKS NAME CLASS')
for i in range(n):
    a=r(input(),input(),input(),input())
    sum+=int(a.MARKS)
c=(sum//n)
print("{:.2f}".format(c))
