def combine_anagrams(words_array):
    res = []
    temp_array = ' '.join(words_array).split(' ')
    index_currentWord = 0
    while temp_array != []:
        currentWord = temp_array[0]
        temp_array.pop(0)
        res.append([currentWord])
        a = set()
        for j in currentWord:
            a.add(j)
        lenOfCurWord = len(currentWord)
        g = temp_array.copy()
        # Цикл по словам в temp_array
        te = set()
        for i in range(len(g)):
            # Флаг для проверки на анаграмму
            flag = True
            # Цикл по буквам в слове

            for k in range(len(g[i])):
                # Если хотя бы одна буква не сходится, то пропускаем слово
                if g[i][k] not in a:
                    #Не подходит
                    flag = False
                    break
            # Слово подошло и его можно исключить из temp_array
            if flag and lenOfCurWord == len(g[i]):
                te.add(i)
                res[index_currentWord].append(g[i])
        temp_array = [temp_array[i] for i in range(len(temp_array)) if i not in te]
        index_currentWord += 1
    return res



print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar","creams", "scream"]))
#=> [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] ]
