def prime(n,i=2):
    if n==1:
        return 0
    if n==2:
        return 1
    
    if n%i==0:
        return 0
    if i*i>n:
        return 1
    return prime(n,i+1)

a=int(input())
r=prime(a)
if r==1:
    print('primee')
else:
    print('Not primee')
