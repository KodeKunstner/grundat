# -*- coding: utf-8 -*-

import timeit

def get_time(sort_fun, *args, **kwargs):
    # Tag tid på sorteringen
    def fun():
        sort_fun(*args, **kwargs)
    time = timeit.Timer(fun).timeit(1)
    return (sort_fun.__name__, time)
