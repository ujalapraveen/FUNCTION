#Break
def prime (num):
    i=1
    while i<=num:
        count=0
        j=2
        while j<i:
            if i%j==0:
                count=count+1
                break
            j=j+1
        if count==0:
            print(i,"prime no")
        i=i+1
num=int(input("enter a num"))
prime(num)


#without using break

# def prime(num):
#     i=1
#     while i<=num:
#         count=0
#         j=2
#         while j<i:
#             if i%j==0:
#                 count=count+1
#             j+=1
#         if count==0:
#             print(i,"prime no")
#         i+=1
# num=int(input("enter a no"))
# prime(num)
        