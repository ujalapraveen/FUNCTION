# #Question(part1)

# # def ask_question():
# #     print("text")
# # ask_question()
# # ask_question()
# # ask_question()
# # ask_question()
# # ask_question()

# #Question(part2)

# def question():
#     i=1
#     while i<=100:
#         print(i,"text")
#         i=i+1
# question()

# #Question(3) part1

# def student(*name):
#     for name in name :
#         print(name)
# student("ujala","Megha","Gouri","Anzum","sristhi")

# #Question(3) part2

# def GreaterThen20(a,b=20):
#     print(a,b)
# GreaterThen20(10)

# #Question(4) part1
 
# def add_numbers(num1,num2):
#      result=num1+num2
#      print(result)
# num1=56
# num2=12
# add_numbers(num1,num2)

# #Question(4) part2

# def add_numbers_list(a,b):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=a[i]+b[i]
#         i=i+1
#         print(sum)
# a=[50,60,10]
# b=[10,20,13]
# add_numbers_list(a,b)

# #Question(5) part1

# def check_numbers(num1,num2):
#     if num1%2==0 and num2%2==0:
#         print("dono even hai")
#     else:
#         print("dono numbers even nahi hai")
# num1=int(input("enter a num"))
# num2=int(input("enter a no"))
# check_numbers(num1,num2)

#Question(5) part2

def check_numbers_list(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("even hai")
        else:
            print("not even")
        i=i+1
a=[2,6,18,10,3,75]
b=[6,19,24,12,3,87]
check_numbers_list(a,b)








