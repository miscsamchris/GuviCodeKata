k=int(input())
narr=[]
for i in range(k):
    narr.extend(input().split())
narr=[int(x) for x in narr]
narr.sort()
for i in narr: print(i,end=" ")
