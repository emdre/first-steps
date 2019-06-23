def higher_than(value_list, n):
    lst = []
    for value in value_list:
        if value > n:
            lst.append(value)
    return(lst)

#test
list1 = [0, 1, 2, 3, 4, 5, 6]
print(higher_than(list1, 3))
