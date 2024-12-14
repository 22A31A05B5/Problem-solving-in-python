def countt(n,c=0):
    if n==0:
        return c
    else:
        return countt(n//10,c+1)

def arm(n,c):
    if n==0:
        return 0
    d=n%10
    return d**c+arm(n//10,c)

def armstrong(n):
    c=countt(n)
    return n==arm(n,c)

n=int(input())
if armstrong(n):
    print("Armstrong number")
else:
    print("Not Armstrong number")

    
