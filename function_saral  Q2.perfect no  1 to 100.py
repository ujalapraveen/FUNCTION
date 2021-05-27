 
#In user input if gave anu number find perfect no

def perfct(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print("perfect no")
    else:
        print("not perfect no")
num=int(input("enter a no"))
perfct(num)



# 1 to 1000 between perfect no


def perfect(num):
    i=1
    while i<=num:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print(i,"perfect no")
        i+=1
num=int(input("enter a no"))
perfect(num)



