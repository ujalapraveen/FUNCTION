def sumaverg(num):
    i=0
    sum=0
    while i<num:
        num1=int(input("enter a no"))
        sum=sum+num1
        i=i+1
    average=sum/num
    print(sum)
    print(average)
num=int(input("enter a no"))
sumaverg(num) 