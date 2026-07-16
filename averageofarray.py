def averageofarray(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]

    average=sum//len(arr)

    return average
arr=[10,10,10,10,10]
print(averageofarray(arr))