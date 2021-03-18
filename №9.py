def connect_dicts(hash1, hash2):
    first_sum = sum(hash1.values())
    second_sum = sum(hash2.values())
    out = list(filter(lambda x: x in hash1, hash2))
    temp_dict1 = hash1.copy()
    temp_dict2 = hash2.copy()
    res = []
    if out != []:
        for key, val in hash1.items():
            for k, v in hash2.items():
                if key == k:
                    if first_sum > second_sum:
                        res.append((key, val))
                        temp_dict1.pop(key)
                        temp_dict2.pop(k)
                    elif first_sum < second_sum:
                        res.append((k, v))
                        temp_dict2.pop(k)
                        temp_dict1.pop(key)
                    elif first_sum == second_sum:
                        res.append((k, v))
                        temp_dict2.pop(k)
                        temp_dict1.pop(key)

    temp_arr2 = list(temp_dict2.items())
    temp_arr1 = list(temp_dict1.items())

    rest = res + temp_arr1 + temp_arr2
    r = list(filter(lambda x: x[1] >= 10, rest))
    r.sort(key=lambda x: x[1])
    return r



print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }
