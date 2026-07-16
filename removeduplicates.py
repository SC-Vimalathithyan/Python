def removeduplicates(arr):
    arr.sort()

    removeduplicates=set(arr)

    return removeduplicates



arr=[1,2,3,4,5,1,2,3]
print(removeduplicates(arr))