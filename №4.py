def sort_list(array):
    if len(array) < 1:
        return []
    a = sorted(array)
    b = array.copy()
    fI = a[0]
    lI = a[-1]
    for i in range(len(array)):
        if array[i] == fI:
            b[i] = lI
        if array[i] == lI:
            b[i] = fI
    b.append(fI)
    return b


"""
print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]
"""
