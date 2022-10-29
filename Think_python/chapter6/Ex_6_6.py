def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False

word = str(input("Enter the word \n"))
result = is_palindrome(word)
print(result)