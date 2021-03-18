def coincidence(array=None, rang=None):
    if rang is None or array is None:
        return []
    res = []
    for i in array:
        if (isinstance(i, int) or isinstance(i, float)) and i >= rang[0] and i < rang[-1]:
           res.append(i)
    return res



print(coincidence([1, 2, 3, 4, 5], (3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], (1, 4))) # => [1, 2, 2.5]
