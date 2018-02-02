# 피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 
# 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.
# 예제)
# Input: N = 12
# Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
import array
import bisect

def question(inputValue):

    n = 0
    n_1 = 1
    even = array.array('I', [])

    if n_1 < inputValue:
        while n_1 < inputValue:
            n, n_1 = n_1, n_1 + n
            if n_1 % 2 == 0:
                even.append(n_1)
    position = bisect.bisect(even, inputValue)
    print('정답', sum(even[:position + 1]))

question(int(input()))