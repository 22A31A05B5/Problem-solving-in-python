def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    print(m)

x=int(input())
y=int(input())

fun(x,y)
