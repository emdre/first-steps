def biggest_element(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] > lst[1]:
            lst.pop(1)
            return biggest_element(lst)
        else:
            lst.pop(0)
            return biggest_element(lst)
