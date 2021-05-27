def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even no")
        else:
            print(i,"odd no")
        i=i+1
limit=int(input("enter a no"))
showNumbers(limit)