# given a string with brackets!! say : {(a+b)+c}
# we have to check if the string is para balanced!!

# order of the brackets matters : {( )} : Correct
#                               : {( }) : Incorrect

# So we can follow LIFO : what comes first goes last : {, (, ), }


def checkRedundant(str):
    s = []

    for char in str:
        if char is '(':
            if len(s)<=1:
                continue
            elif (s[-1]=='('):           #not s means: if nothing is in s !!
                return True
        elif char is ')':
            if s[-1]== '(':
                return True
        s.append(char)



    return False

str=input()
if checkRedundant(str):
    print('true')
else:
    print('false')

# Example :((a+b))
# Solution: True

# assumed : EQn is balanced
