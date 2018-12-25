from functools import reduce
n,k=input().split()
n,k=int(n),int(k)
ar=input()
ar=[int(x) for x in ar.split()]
if n>1:
    ans=reduce(lambda x,y: x or y,[ar[x]+ar[y]==k for x in range(n) for y in range(n) if x!=y ])
else:
    ans=ar[0]==k
if ans:
    print("yes")
else:
    print("no")
