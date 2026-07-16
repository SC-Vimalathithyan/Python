def reversearr(arr):
    reversed_arr=arr[::-1]

    return reversed_arr
arr=[1,2,3]
print(reversearr(arr))


def reverse(Arr):
    reversed_arr=[]
    for i in range(len(Arr)-1,-1,-1):
        reversed_arr.append(arr[i])

    return reversed_arr

print(reverse(arr))