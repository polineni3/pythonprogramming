a,b=map(int,input().split())
l=[]
for val in range(a+1,b ):
  if val > 1:
    for m in range(2,val):
      if(val % m) == 0:
        break
    else:
      l.append(val)
for n in range(0,len(l)):
  if(n==len(l)-1):
    print(l[n],end="")
  else:
    print(l[n],end=" ")
