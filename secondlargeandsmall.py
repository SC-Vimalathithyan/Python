def sort(arr):
    if len(arr)==0:
        return None
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(arr[i]<arr[j]):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
    return arr

arr=[1,9,2,4,6,10,8,7]
sort(arr)
print(arr[-2],arr[1])
