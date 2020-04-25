n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    c=input().split()
    if c[0]=="pop":
        s.pop()
    elif c[0]=="remove":
        s.remove(int(c[1]))
    elif c[0]=="discard":
        s.discard(int(c[1]))

if len(s)==0:
    print(0)
else:
    print(sum(s))
