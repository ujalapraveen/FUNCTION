def palindrom_no(a):
    if a==a[::-1]:
        print("it is palindrom no")
    else:
        print("it is not palindrom no")
palindrom_no(a=(input("enter a no")))