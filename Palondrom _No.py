# def palindrom_No(string):
#     rev=[]
#     index=-1
#     while index>=(-len(string)):
#         rev.append(string[index])
#         index=index-1
# string=int(input("enter a no"))
# palindrom_No(string)


def ispalindrome (string):
    left_pos=0
    right_pos=len(string)-1
    while right_pos >=left_pos:
        if not string[left_pos]==string[right_pos]:
            return False
        left_post =left_post+1
        right_post= right_post-1
    return True
print(ispalindrome("aza"))