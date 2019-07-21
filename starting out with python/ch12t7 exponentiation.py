def exponentiate(x,y):
    if y == 0:
        return 1
    else:
        return x * exponentiate(x, y - 1)

