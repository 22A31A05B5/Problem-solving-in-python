def fun(a):
    if a==0:
        return 200
    print(a)
    fun(a-1)
x=int(input())
fun(x)
