
def string_reverse(str1):
    rstr1= ''
    i=len(str1)
    while i >0:
        rstr1+=str1[i-1]
        i=i-1
    return rstr1
print(string_reverse("1234abcd"))




