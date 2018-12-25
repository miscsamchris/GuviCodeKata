def asciitoindex(n):
    return ord(n)-96
try:
    st1=str(input())
    st2=str(input())
    st1=st1.lower()
    st2=st2.lower()
    nr=[]
    x=1
    for i,j in zip(st1,st2):
        if x%2==0:
            nr.append(chr((asciitoindex(j)+asciitoindex(i))%27 +int((asciitoindex(j)+asciitoindex(i))/27)+96))
        else:
            nr.append(chr((asciitoindex(i)+asciitoindex(j))%27 +int((asciitoindex(j)+asciitoindex(i))/27)+96))
        x+=1
    print("".join(nr))
except:
    pass
