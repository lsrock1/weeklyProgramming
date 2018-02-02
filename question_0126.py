def question(inputs):
    
    subArraySum = inputs[0]
    midSum = 0

    for value in inputs[1:]:
        
        midSum = value + midSum
        if(midSum > 0):
            subArraySum = subArraySum + midSum
            midSum = 0

        if(value > subArraySum):
            subArraySum = value

    return subArraySum

def main():
    a = [-1, 3, -1, 5]
    b = [-5, -3, -1]
    c = [2, 4, -2, -3, 8]
    d = [a, b, c]
    for i in d:
        print(question(i))

main()