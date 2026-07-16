def minimuminarray(arr):
    min=arr[0]
    if len(arr)==0:
        return None
    else:
        for i in range(len(arr)):
            if (arr[i]<min):
                min=arr[i]
    
    return min

arr=[1,2,3,4,5]
print(minimuminarray(arr))