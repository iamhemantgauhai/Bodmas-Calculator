def normalsolver(lis): #function which solves simple expression like 3+2/4-6x6 without brackets
    while '/' in lis: # To perform all divide operations first
        ind=lis.index('/')
        answer=lis[ind-1]/lis[ind+1]
        lis[ind-1:ind+2]=[answer]
    while 'x' in lis: # Then to perform all multiplication operations 
        ind=lis.index('x')
        answer=lis[ind-1]*lis[ind+1]
        lis[ind-1:ind+2]=[answer]
    while '+' in lis: # Then to perform all addition
        ind=lis.index('+')
        answer=lis[ind-1]+lis[ind+1]
        lis[ind-1:ind+2]=[answer]
    while '-' in lis: # Then to perform all subtraction
        ind=lis.index('-')
        answer=lis[ind-1]-lis[ind+1]
        lis[ind-1:ind+2]=[answer]
    return lis
def main_program():
    try:
        inp=input("Enter expression : ")
        lis=[]
        s=''
        for i in inp: # To construct a proper list of the expression
            if i.isdigit() or i=='.':
                s+=i
            elif i in ['/','+','-','x','(',')']:
                if s!='':
                    lis.append(float(s))
                if i=='(':
                    if isinstance(lis[-1],float): # To handle OF in BODMAS
                        lis.append('x')
                s=''
                lis.append(i)
        if s!='':
            lis.append(float(s))
        while '(' in lis: # To grab inner brackets and solve them with normalsolver function
            close_brack = lis.index(')') # Index of inner closing brackets
            open_brack = len(lis)-lis[::-1].index('(')-1 #index of inner opening brackets
            new_list=lis[open_brack+1:close_brack] #Selecting the normal expression in inner brackets
            answer=normalsolver(new_list) #Solving the simple expression with normalsolver
            lis[open_brack:close_brack+1]=answer # Changing the inner bracket now with it's answer
        final_answer=(normalsolver(lis))[0] 
        print(final_answer, 'is the final answer')
        return final_answer
    except:
        raise Exception("You crashed the calulator by giving wrong input :-/")

if __name__ == "__main__":
    main_program()