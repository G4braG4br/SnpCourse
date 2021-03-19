def max_odd(lis):
    maxi = 0
    res = None
    for i in lis:
        if type(i) == int or type(i) == float:
            if i%2 != 0 and abs(i) > maxi:
                maxi = int(i)
                res = maxi
    return res



print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None
