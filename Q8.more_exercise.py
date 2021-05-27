def new_list(list_1,list_2):
    i=0
    c=list_1+list_2
    a=[]
    while i <len(c):
        if c[i] not in a:
            a.append(c[i])
        i=i+1
        a.sort()
    print(a)
list_1=[1,5,10,12,16,20]
list_2=[1,2,10,13,16]
new_list(list_1,list_2)
    
  