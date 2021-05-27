def function_calculate(num):
    fac=1
    while num>0:
        fac=fac*num
        num=num-1
    return fac
num=int(input("enter a no"))
print(function_calculate(num))

