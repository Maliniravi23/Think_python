def is_palindrome(word):
    return word == word[::-1]


result = is_palindrome("madam")
print(result)
