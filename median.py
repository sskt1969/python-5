ch=int(input(""))
list=[int(x) for x in input().split()]
ch1=0
for i in range(0,ch):
    ch1+=list[i]
print(int(ch1/ch))
