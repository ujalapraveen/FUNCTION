def harsad_no(num):
    sum=0
    a=num
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    if a%sum==0:
        print("harsad no")
    else:
        print("not harsad no")
num=int(input("enter a no"))
harsad_no(num)

    
