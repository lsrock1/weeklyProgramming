# 정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).
# ﻿
# 예제}
# Input: [-1, 3, -1, 5]
# Output: 7 // 3 + (-1) + 5

# Input: [-5, -3, -1]
# Output: -1 // -1

# Input: [2, 4, -2, -3, 8]
# Output: 9 // 2 + 4 + (-2) + (-3) + 8
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