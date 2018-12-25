from functools import reduce
n,k=input().split()
n,k=int(n),int(k)
ar=input()
ar=[int(x) for x in ar.split()]
ans=reduce(lambda x,y: x or y,[ar[x]+ar[y]==k for x in range(n) for y in range(n) if x!=y ])
if ans:
    print("yes")
else:
    print("no")
