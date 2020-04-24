n=int(input())
for i in range(n):
    try:
        a,b=input().split()
        print(int(a)//int(b))
    except BaseException as e:
        print("Error Code:",e)
   
