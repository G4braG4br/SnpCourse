def count_words(string):
    word = ''
    tmp = []
    string += "$"
    for i in string:
        if i.isalpha():
            word += i
        else:
            if word:
                tmp.append(word.lower())
                word = ''
    d = {}
    for i in tmp:
        d[i] = tmp.count(i)
    return d



print(count_words("A man, a plan, a canal -- Panama")) # => {"a" => 3, "man" => 1,"canal" => 1, "panama" => 1, "plan" => 1}
print(count_words("Doo bee doo bee doo")) # => {"doo" => 3, "bee" =>2}
