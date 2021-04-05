def is_palindrome(string=None):
    if isinstance(string, type(None)):
        return False
    string = str(string)
    a = ''.join(i for i in string if i.isalnum()).upper()
    if a == "" or len(a) == 1:
        return True
    for i in range((len(a) - 1)//2):
        if a[i] != a[-i-1]:
            return False
    return True


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
