def stockSpan(price,n):
    s = []
    output = []
    s.append(0)
    output.append(1)
    for i in range(1,len(price)):
        while(len(s)!=0 and price[s[-1]] < price[i]):
            s.pop()
        if(len(s) == 0):
            output.append(i+1)
        else:
            output.append(i-s[-1])
        s.append(i)
    return output
#main
n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')