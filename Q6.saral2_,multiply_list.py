#multiple_list=list_change([5,10,50,20],[2,20,3,5])
def multiple_list(a,b):
    i=0
    list=[]
    while i<len(a):
        multi=a[i]*b[i]
        list.append(multi)
        i=i+1
    print(list)
a=[5,10,50,20]
b=[2,20,3,5]
multiple_list(a,b)


