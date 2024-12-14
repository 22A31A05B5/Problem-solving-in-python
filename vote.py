n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
res=[]
for i in range(n):
    if l2[i]>=18:
        res.append(l1[i])
ca1=res.count(1)
ca2=res.count(2)
ca3=res.count(3)
if ca1==ca2 and ca2==ca3 and ca1==ca3:
    print("Draw")
else:
    m=max(ca1,ca2,ca3)
    print(m)
