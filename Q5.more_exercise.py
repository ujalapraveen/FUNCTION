def factorial(i):
    fac=1
    while i>0:
        fac=fac*i
        i=i-1
    print(fac)
i=int(input("enetr a no"))
factorial(i)