def sum_elements(n):
    if n <= 1:
        return n
    else:
        return n + sum_elements(n - 1)


