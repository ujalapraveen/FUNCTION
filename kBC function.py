que_list = [".How many continents are there?",".What is the capital of India?",       ".NG mei kaun se course padhaya jaata hai?"]
opt_list= [["Four", "Nine", "Seven", " Eight"],[" Chandigarh", "Bhopal", " Chennai", "Delhi"],["Software Engineering", " Counseling", "Tourism", "Agriculture"]]
ans_list=[3,4,1]
fifty_list=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering']]
sol_list=[3,4,1]  
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('enter the num'))
        lifelinecount+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"    
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('enter the option'))
    if user_ans==ans_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        if result == "no":
            index-=1
        elif result==True:
            print("congratulation")
        else:
            print("you losee")
            break 
        index+=1

def main():
    que()
main()
