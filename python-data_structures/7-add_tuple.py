#!/usr/bin/python3
def add_tuple(tuple_x=(), tuple_y=()):
    x = tuple_x[0] if len(tuple_x) > 0 else 0
    y = tuple_y[0] if len(tuple_y) > 0 else 0

    x1 = tuple_x[1] if len(tuple_x) > 1 else 0
    y1 = tuple_y[1] if len(tuple_y) > 1 else 0

    return (x+y, x1+y1)