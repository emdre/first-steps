def print_stars(n):
    if n > 1:
        print_stars(n - 1)
        print('*' * n)
    else:
        print('*')
