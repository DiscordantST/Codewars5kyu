def move_zeros(lst):
    zero = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.remove(lst[i])
            lst.append(zero)
    return lst
