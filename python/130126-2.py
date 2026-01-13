def ret_max(arr):
    maxvalue = arr[0]
    for num in arr:
        if num > maxvalue:
            maxvalue = num
    return maxvalue

arr = [3, -1, 0, 17, -5, 2]
print(ret_max(arr))