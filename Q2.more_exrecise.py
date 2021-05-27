#FIRST METHOD


# def total_Budget(a,b):
#     if a*b>=50000:
#         return"hum budget ke ander hai"
#     if a*b<=50000:
#         return "hum budget ke outside hai"
#     else:
#         pass
# a=int(input("enter a number of students"))
# b=int(input("enter a number of expenses"))
# print(total_Budget(a,b))


#SECOND METHOD

def budget(amount,student):
    c=len(student)
    total=c*amount
    if amount<=50000:
        print(total,"uderbudget")
    else:
        print(total,"overbudge")
amount=int(input("enter the amount"))
budget(amount,["ujala","Megha","Anzum","Shubhangi","Anzum"])
