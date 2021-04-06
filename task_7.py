
def combine_anagrams(array_of_words=None):
    if array_of_words is None or len(array_of_words) <= 1:
        return None
    result_array = []
    index_of_current_word = 0
    while array_of_words != []:
        current_word = array_of_words[0]
        temp_current_word = ''.join(sorted(array_of_words[0].lower()))
        array_of_words.pop(0)
        result_array.append([current_word])
        indexes_of_words_to_remove = []
        for i in range(len(array_of_words)):
            if ''.join(sorted(array_of_words[i].lower())) == temp_current_word:
                indexes_of_words_to_remove.append(i)
                result_array[index_of_current_word].append(array_of_words[i])
            else:
                continue
        if indexes_of_words_to_remove != []:
            array_of_words = [array_of_words[i] for i in range(len(array_of_words)) if i not in indexes_of_words_to_remove]
        index_of_current_word += 1

    return result_array



print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
# => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] ]
print(combine_anagrams(['cara', 'arca', 'lava', 'alava', 'val', 'lav']))
# => [['cara', 'arca'], ['lava'], ['alava'], ['val', 'lav']]
print(combine_anagrams(['agal', 'aggl'])) # => [['agal'], ['aggl']])
print(combine_anagrams(['', '']))
print(combine_anagrams())

