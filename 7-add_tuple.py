def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    new_x = tuple_a[0] + tuple_b[0]
    new_y = tuple_a[1] + tuple_b[1]
    new_tuple = (new_x, new_y)
    return new_tuple
