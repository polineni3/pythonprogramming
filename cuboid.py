L,B,H=map(int,input().split())
S=L*B*H
V=2*(L*B+B*H+L*H)
p=S
if(p==S):
  print(V,S,end="")
