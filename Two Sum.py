def two_sum(arr, target):
    for i in range(len(arr)):
        for n in range(i+1, len(arr)):
            if (arr[i] + arr[n]) == target:
                return i, n
    return False

print(two_sum([1,2,3,4,5,6],7))

def two_sum_v2(arr, target):
    aux1 = {}

    for i, n in enumerate(arr):
        dif = target - n
        if dif in aux1:
            return i, aux1[dif]
        aux1[n] = i
    return

print(two_sum_v2([1,2,3,4,5,6],7))
