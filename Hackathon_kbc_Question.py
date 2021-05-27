question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1] 
fifty_fifty = [['1.Four','3.seven'],['2.Bhopal','4.Delhi'],['1.Software Engineering','2.Counseling']]

fifty_fifty_used = True
i=0

def printQuestions(index):
    print(question_list[index])

def printFiftyFiftyOptions(index):
    print(fifty_fifty[index])

def isAnswerCorrect(input):
    return input== solution_list[i]

def printOptions(index):
    j=0
    while j<len(options_list[index]):
        print(options_list[index][j])
        j=j+1

def userChooseFiftyFifty(input):
    return input==5050

def isFiftyFiftyAvailable():
     return fifty_fifty_used 

def fiftyFiftyUsed():
    fifty_fifty_used=False 

print("you have 5050 lifeline,if you want you can use it be entering'5050'")

while i<len(question_list):
    printQuestions(i)
    printOptions(i)

    user_input=int(input("enter your number option:"))
    if isAnswerCorrect(user_input):
        print('congrats')
    else:
        if userChooseFiftyFifty(user_input):
            if isFiftyFiftyAvailable():
                printFiftyFiftyOptions(i)
                fiftyFiftyUsed()
                user_input_fifty_fifty=int(input("enter your option now"))
                if isAnswerCorrect(user_input_fifty_fifty):
                    print("congrats!,you choice correct option")
                else:
                    print("sadly!,you choice wrong option")
            else:
                print("you used fifty fifty,so please enter your own answer")
        else:
            print("oops!your answer is wrong")
            print('quit') 
            
    i=i+1 







