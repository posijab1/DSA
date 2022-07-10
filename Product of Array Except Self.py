def ProductofArrayExceptSelf(array):
    l, r = 1, 1
    answer = [0] * len(array)

    for i in range(len(array)):
        answer[i] = l
        l *= array[i]
    for i in range(len(array)-1,-1,-1):
        answer[i] *= r
        r *= array[i]
    return answer

print(ProductofArrayExceptSelf([1,2,3]))

def ProductofArrayExceptSelf_BruteForece(array):
    answer = []

    for i in array:
        auxiliary_answer = 1
        for n in array:
            auxiliary_answer *= n
        answer.append(int(auxiliary_answer/i))
    return answer

print(ProductofArrayExceptSelf_BruteForece([1,2,3]))


