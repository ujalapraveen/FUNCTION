def function_calculate(a):
    i=0
    duplicate=[]
    while i<len(a):
        if a[i]not in duplicate:
            duplicate.append(a[i])
        i=i+1
    print(duplicate)
function_calculate([1,2,3,3,3,3,4,5])
