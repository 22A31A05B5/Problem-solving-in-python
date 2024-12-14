def dig(n,r=0):
    if n==0:
        return r
    else:
        d=n%10
        r=r+d
        return dig(n//10,r)


a=int(input())
print(dig(a))
