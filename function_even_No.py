def even_No(a):
    i=1
    enum=[]
    while i< len(a):
        if a[i]%2==0:
            enum.append(a[i])
        i=i+1
    print(enum)    
even_No([1,2,3,4,5,6,7,8,9])
