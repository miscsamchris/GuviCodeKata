st=str(input())
for i in range(1,len(st)):
    if st[i:]>st:
        print(st[i:])
        break
