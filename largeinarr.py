def largestinarray(arr):
    max=arr[0]
    if(len(arr)==0):
        return None
    else:
        for i in range(len(arr)):
            if(arr[i]>max):
                max=arr[i]

    return max

arr=[1,2,3,4,5,6,7,8]
print(largestinarray(arr))