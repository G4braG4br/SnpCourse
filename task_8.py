def multiply_numbers(*inputs):
    isnum = None
    forint = 1

    for i in inputs:

        if type(i) is list or type(i) is tuple or type(i) is set:
            for el in i:

                if type(el) is int:
                    forint *= el
                    isnum = forint
                elif type(el) is float:
                    temp = multiply_numbers(el)
                    forint *= temp
                    isnum = forint
                elif type(el) is list:
                    temp = multiply_numbers(el)
                    forint *= temp
                    isnum = forint

        if type(i) is int:
            forint *= i
            isnum = forint

        if type(i) is float:
            lis = str(i)
            for el in lis:
                if el.isdigit():
                    forint *= int(el)
                    isnum = forint

        if type(i) is str:
            for el in i:
                if el.isdigit():
                    forint *= int(el)
                    isnum = forint

    return isnum



print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120
print(multiply_numbers([[[[2]]]], "@34", 3, [2.2, 2], (2, 3.3), {2, 3})) # => 62 208
