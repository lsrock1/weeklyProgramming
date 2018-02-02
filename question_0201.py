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