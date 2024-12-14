n=input()
res=''
tfi=''
for i in n:
    if n.count(i)>=2 and i not in res:
        res+=(i*2)
    if n.count(i)==1:
        tfi=tfi+i
        
print(res+tfi)
