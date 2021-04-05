def multiply_numbers(inputs=None):
    isnum = None

    if inputs is None:
        return None

    if type(inputs) is list:
        re = 1
        for i in inputs:

            if type(i) is int:
                re *= i
                isnum = re
            elif type(i) is float:
                temp = multiply_numbers(i)
                re *= temp
                isnum = re
            elif type(i) is list:
                temp = multiply_numbers(i)
                re *= temp
                isnum = re
        return isnum

    if type(inputs) is float:
        lis = str(inputs)
        res = 1
        for i in lis:
            if i.isdigit():
                res *= int(i)
                isnum = res
        return isnum

    if type(inputs) is str:
        res = 1
        for i in inputs:
            if i.isdigit():
                res *= int(i)
                isnum = res

    return isnum



print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120
