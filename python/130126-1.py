def dict_accept(arr):
    posit = negat = zeroes = 0
    for num in arr:
        if num > 0:
            posit += 1
        elif num < 0:
            negat += 1
        else:
            zeroes += 1
    return {"positive":posit, "negative":negat,"zero":zeroes}

arr = [3, -1, 0, 7, -5, 0, 2]
dic = dict_accept(arr)
print(dic)