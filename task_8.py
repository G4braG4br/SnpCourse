from collections.abc import Iterable
from functools import reduce


def multiply_numbers(*inputs):
    isnum = None
    forint = 1
    for i in inputs:
        if isinstance(i, Iterable):
            for el in i:
                if isinstance(el, str):
                    for char in el:
                        if char.isdigit():
                            forint *= int(char)
                            isnum = forint
                else:
                    temp = multiply_numbers(el)
                    if isinstance(temp, int) or isinstance(temp, float):
                        forint *= temp
                        isnum = forint

        elif type(i) is int:
            temp = multiply_numbers(str(i))
            forint *= temp
            isnum = forint

        elif type(i) is float:
            temp = multiply_numbers(str(i))
            forint *= temp
            isnum = forint

    return isnum


def multiply_numbers2(*args):
    return reduce(lambda x, y: x * y, list(int(i) for i in str(args) if i.isdigit()) ) if ( True in list(map(lambda x: x.isdigit(), str(args))) != [] ) else  None


#print(multiply_numbers([[[[[2]]]], "@34", 3, [2.2, 2], (2, 3.3), {2, 3}])) # => 62 208
#print(multiply_numbers({2: 3}))

