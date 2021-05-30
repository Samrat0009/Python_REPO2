#def bracketReversal(str):
#    up = 1
#    down = 1
#    for ele in str:
#        if ele in '{':
#            up+=1
#        elif ele in '}':
#            down+=1
#
#    if (up>=down):
#        return (up-down)//2
#    else:
#        return -(up-down)//2

#str = input()
#if len(str)%2!=0:
#    print(-1)
#else:
#    out = bracketReversal(str)
#    print(out)


# solution:

def reversal(string):
    s = []
    l = len(string)
    if l % 2 != 0:
        return -1
    for ele in string:
        if len(s) == 0:
            s.append(ele)
        elif ele is "{":
            s.append(ele)

        elif ele is "}" and s[-1] != "{":
            s.append(ele)
        else:
            s.pop()
    count = 0
    while len(s):
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count = count + 2
        else:
            count = count + 1
    return count


string = input()
print(reversal(string))