c=int(input())
if(c<=1000):
    storage=input()
    storage=[int(x) for x in storage.split()]
    kk=sorted(storage[0:c])
for i in range(0,c):
    if(i<c-1):
        f=' '
    else:
        f=' '
    print(kk[i],end=f)
