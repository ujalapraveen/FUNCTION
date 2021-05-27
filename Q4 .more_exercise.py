def num(a,b,c):
    if a>b and a>c :
        print(a,"greatest")
    elif b>a and b>c:
        print(b,"greatest")
    elif c>a and c>b:
        print(c,'greatest')
    
a=int(input("enter a first num"))
b=int(input("enter a second no"))
c=int(input("enter a third no"))
num(a,b,c)




