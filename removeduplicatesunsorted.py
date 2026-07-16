def remove_duplicates(arr):
    result=[]

    for i in arr:
        duplicate=False

        for j in result:
            if i==j:
                duplicate=True
                break
        if not duplicate:
            result.append(i)
    return result

arr=[4,2,4,1,1,5,6,7]
print(remove_duplicates(arr))