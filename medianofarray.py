def medianofarray(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 0:
        med = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        med = arr[n//2]

    return med

arr = [1, 3, 4]
print(medianofarray(arr))