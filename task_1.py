def is_palindrome(string=None):
    if string is None:
        return False
    a = ''.join(i for i in str(string) if i.isalnum()).upper()
    return a == a[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
