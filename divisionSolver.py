x = [[16,[8,2],4],2,80]
y = []
def resolveArray(input):
    
    for i in input:
        if type(i) is list:
            if len(i) == 2:
            
                y.append(i[0]/i[1])
            else:
                resolveArray(i)
        else:
            y.append(i)
    return y

def divisionSolver(input):

    k = resolveArray(input)
    result = k[0]
    for j in range(len(k)-1):
        result = result/k[j+1]
    return result


print("-------")
print(divisionSolver(x))