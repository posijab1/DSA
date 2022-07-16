def Two_Sum(array, target):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]

#print(Two_Sum([1,2,3,4,5,6,7], 13))


def twoSum(array, target):
    hashMap = {}
    for i, n in enumerate(array):
        difference = target - n
        if difference in hashMap:
            return [hashMap[difference], i]
        hashMap[n] = i

print(twoSum([1,2,3,4,5,6,7], 10))