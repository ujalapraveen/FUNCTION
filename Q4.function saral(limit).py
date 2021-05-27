def show_Numbers(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print(i,"evevn no")
        else:
            print(i,"odd no")
        i+=1
limit=int(input("enter a no"))
show_Numbers(limit)