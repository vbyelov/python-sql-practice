def count_even_odd(arr):
    odd = even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return {"even":even, "odd":odd}

print(count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))