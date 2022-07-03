def contain_duplicates(arr):
    for i in range(len(arr)):
        for n in range(i+1, len(arr)):
            if arr[i] == arr[n]:
                return True
    return False

print(contain_duplicates([1,2,3,4]))



def contain_duplicates2(arr):

    aux1 = set()
    for i in arr:
        if i in aux1:
            return True
        aux1.add(i)
    return False

print(contain_duplicates2([1,2,3,4]))