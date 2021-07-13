def max(n):
    i=0
    max=0
    while i<len(n):
        if n[i]>max:
            max=n[i]
        i+=1
    return(max)

def checkmax(even,odd):
    m=even+odd
    k=max(m)
    return k


def even(a):
    i=0
    c=[]
    d=[]
    while i <len(a):
        if a[i]%2==0:
            c.append(a[i])
    
        else:
            d.append(a[i])
    
        i=i+1
    print(c)
    print(d)
    l=checkmax(c,d)
    print(l)
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even(a)




    




