# given a string with brackets!! say : {(a+b)+c}
# we have to check if the string is para balanced!!

# order of the brackets matters : {( )} : Correct
#                               : {( }) : Incorrect

# So we can follow LIFO : what comes first goes last : {, (, ), }


def checkBalanced(str):
    s = []
    for char in str:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1]!='('):           #not s means: if s is not in array !!
                return False
            s.pop()                       
        elif char is '}':
            if (not s or s[-1] != '{'):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
       return True
    return False

str=input()
if checkBalanced(str):
    print('true')
else:
    print('false')

# Example :[(a+B+c)+c}]
# Solution: false
