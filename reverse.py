def rev(n,r=0):
    if n==0:
        return r
    else:
        d=n%10
        r=r*10+d
        return rev(n//10,r)


a=int(input())
print(rev(a))
