def increasing_order(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]<arr[j]):
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr
def decreasing_order(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]>arr[j]):
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr

arr=[3,2,1,6,5,4]
print(increasing_order(arr))
print(decreasing_order(arr))
