ch=int(input())
if(ch<=1000):
    storage=input()
    storage=[int(x) for x in storage.split()]
    kk=sorted(storage[0:ch])
for i in range(0,ch):
    if(i<ch-1):
        f=' '
    else:
        f=' '
    print(kk[i],end=f)
