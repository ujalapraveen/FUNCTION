def strong_password(s):
    if len(s)>=1 and len(s)<=8:
        if "@" in s or "$" in s or "#"in s:
            if "0" or "9" in s:
                if "A" or "Z" in s:
                    print("strong password")
                else:
                    
                    print("week password")
            else:
                print("wrong password")
        else:
            print("wrong")  
    else:
        print("your length is long") 
s=input("enter the password") 
strong_password(s)
    


