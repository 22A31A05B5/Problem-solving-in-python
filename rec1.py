def fun(a):
    if a<=0:
        print(a)
        return 0
    print(a)
    fun(a-1)
    print(a)
x=int(input())
fun(x)
