user=int(input("Choose your language.1.English,2.Hindi....="))
def pin_code():
    if user==1:
        i=0
        while i<3:
            pin=int(input("enter your four digit pin number"))
            if pin==1234:
                print("correct Pin")
                break
            else:
                print("incorrect Pin")
            i+=1
        else:
            print("your card is block!oops")
        return pin
    else:
        i=0
        while i <3:
            pin=int(input("Apna char number ka pin Darj kare="))
            if pin==1234:
                print("Aapka pin sahi hai")
                break
            else:
                print("Fir se apna pin dale")
            i+=1
        else:
            print("Aapka card block ho chuka hai!oops")
        return pin
def english():
    code=pin_code()
    

    if user==1:
        if code==1234:
            Balance=40000
            print("please press 1 for your balance inquiry")
            print("please press 2 for your withdrawl ")
            print("please press 3 for your pay in")
            print("please press 4 for your return card/Exit")
            print("*---------*---------*")
            

            option=int(input("what would you like to choose ="))
            if option==1:
                ans=Balance,"your current balance"
            elif option==2:
                withdrawl=int(input("enter how much money would you like to withdrawl="))
                ans=Balance-withdrawl,"your current balance"
            elif option==3:
                pay=int(input("enter how much money you want to pay in"))
                ans=Balance+pay,"your current balance"
            else:
                ans="collect your card"
                print("THANK YOU FOR VISIT HDFC BANK")
            print(ans)
    else:
        if code==1234:
            Balance=40000
            print('Kripya karke 1 dbaye apni jma rashi ke bare me janne ke lie')
            print('paise nikalne ke lie 2 dbaye')
            print('pese jma karke ke lie 3 dbaye ')
            print('Apna card wapis lele ke lie 4 dabaye')
            print("*-------*--------*")
            print("*-------*--------*")
            option=int(input("Kripya karke apna Viklap chune="))
            if option==1:
                ans=Balance,"Aapki kul jma rashi"
            elif option==2:
                withdrawl=int(input("Aap kitni rashi nikalna chahoge?="))
                ans=Balance-withdrawl,"Aapki kul jma rashi"
            elif option==3:
                pay=int(input("Aap kitna Bhugtan karna chahoge?="))
                ans=Balance+pay,"aapki kul jma rashi"
            else:
                ans="Aapna card jma kar lijiye"
                print("*---------DHANYAWAD AANE KE LIYE----------*")
            print(ans)

english()



