def sum_elements(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_elements(lst[1:])
