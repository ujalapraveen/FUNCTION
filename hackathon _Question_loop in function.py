#. in loop sum

def sum(num):
    i=0
    sum=0
    while i<num:
        num1=int(input("enter a num1"))
        sum=sum+num1
        i=i+1
    return sum
num=int(input("enter a no"))
print(sum(num))

#Q2. in loop prime no

# def prime(num):
#     count=0
#     i=1
#     while i<=num:
#         if num%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         return "prime no"
#     else:
#         return "not prime no"
# num=int(input("enter a no"))
# print(prime(num))

#Q3.inloop perfect no

# def perfect(num):
#     sum=0
#     i=1
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if num==sum:
#         return "perfect no"
#     else:
#         return "not perfect no"
# num=int(input("enter a no"))
# print(perfect(num))

#Q4.in loop in factorial no


# def factorial(num):
#     fac=1
#     while num>0:
#         fac=fac*num
#         num=num-1
#     return fac
# num=int(input("enter a num"))
# print(factorial(num))


#Q5.loop in multiply

# def square(num):
#     i=0
#     while i<num:
#         i=i+1
#     return i**2    
# num=int(input("enter a no"))
# print(square(num))



#Q1. list in function even

# def even(a):
#     i=1
#     enum=[]
#     while i<len(a):
#         if a[i]%2==0:
#             enum.append(a[i])
#         i=i+1
#     return enum
# print(even([1,2,3,4,5,6,7,8,9]))

#Q2.list in function duplicate

# def function_calculate(a):
#     i=0
#     duplicate=[]
#     while i <len(a):
#         if a[i]not in duplicate:
#             duplicate.append(a[i])
#         i=i+1
#     return duplicate
# print(function_calculate([1,2,3,3,3,3,4,4,4,5,5,6,7]))


#Q3.list in function to sum all the numbers in list

# def sum(a):
#     i=0
#     sum=0
#     while i <len(a):
#         sum=sum+a[i]
#         i=i+1
#     return sum
# a=(8,2,3,8,4)
# print(sum(a)) 

#Q4.list in function to multiply all the numbers in a list

# def multiply (a):
#     i=0
#     j=1
#     while i <len(a):
#         j=j*a[i]
#         i=i+1
#     return j
# a=(8,2,3,-1,7)
# print(multiply(a))

#Q5.list all element gave to negative

# def negative(a):
#     i=0
#     j=[]
#     while i<len(a):
#         multi=-1*(a[i])
#         j.append(multi)
#         i=i+1
#     return j
# a=[1,2,3,4,5,-20,-6]
# print(negative(a))


#Q2. DRIVER SPEED

# def driver(speed):
#     speed1=speed-70
#     point=speed1//5
#     if speed<=70:
#         print("ok")
#     elif point>12:
#         print("license suspended")
#     elif speed>70:
#         print(point,"point")
# speed=int(input("enter a speed"))
# driver(speed)





\







