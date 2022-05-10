def minimums(some_dict):
    positions = [] # output variable
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = [] # output variable
            positions.append(k)

    return positions

minimums({'a':1, 'b':2, 'c':-1, 'd':0, 'e':-1})

#['e', 'c']
